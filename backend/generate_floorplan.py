import math
from build123d import (
    BuildPart,
    BuildSketch,
    Locations,
    Mode,
    Plane,
    Rectangle,
    export_stl,
    extrude,
)


def generate_3d_floorplan(
    plan_data: dict,
    scale_ratio: float = 100.0,     # F.eks. 100 for målestok 1:100
    min_wall_mm: float = 1.2,       # Sikkerhedsnet: minimum tykkelse for 3D-print
    include_floor: bool = True,
    output_filename: str = "bygning_model.stl",
):
    """
    Konverterer 2D-plantegningsdata (i virkelige millimeter) til en skaleret,
    printbar 3D-model i millimeter.
    """
    wall_height = plan_data["wall_height_mm"] / scale_ratio
    floor_thickness = 1.5  # Fast 1.5 mm bundplade, så modellen hænger sammen på printpladen

    with BuildPart() as building:
        # 1. OPBYG VÆGGE
        for wall in plan_data["walls"]:
            # Skaler 2D-koordinater fra virkelige mål til print-mål
            x1, y1 = wall["start"][0] / scale_ratio, wall["start"][1] / scale_ratio
            x2, y2 = wall["end"][0] / scale_ratio, wall["end"][1] / scale_ratio

            # Beregn længde og vinkel på væggen
            dx = x2 - x1
            dy = y2 - y1
            length = math.hypot(dx, dy)
            angle_deg = math.degrees(math.atan2(dy, dx))
            mid_x = (x1 + x2) / 2.0
            mid_y = (y1 + y2) / 2.0

            # PRINT-SIKRING: Tving vægtykkelsen op på min_wall_mm, hvis den bliver for tynd
            raw_thickness = wall["thickness_mm"] / scale_ratio
            safe_thickness = max(raw_thickness, min_wall_mm)

            # Tilføj en smule overlap i enderne (safe_thickness), så hjørner smelter rent sammen
            total_length = length + safe_thickness

            # Tegn 2D-rektangel på XY-planet og ekstruder det opad
            with BuildSketch(Plane.XY.offset(floor_thickness if include_floor else 0)):
                with Locations([(mid_x, mid_y)]):
                    Rectangle(total_length, safe_thickness, rotation=angle_deg)

            extrude(amount=wall_height)

        # 2. SKÆR DØRE OG VINDUER UD (Boolean Subtract)
        for opening in plan_data.get("openings", []):
            x1, y1 = opening["start"][0] / scale_ratio, opening["start"][1] / scale_ratio
            x2, y2 = opening["end"][0] / scale_ratio, opening["end"][1] / scale_ratio

            dx = x2 - x1
            dy = y2 - y1
            width = math.hypot(dx, dy)
            angle_deg = math.degrees(math.atan2(dy, dx))
            mid_x = (x1 + x2) / 2.0
            mid_y = (y1 + y2) / 2.0

            sill_height = opening["sill_height_mm"] / scale_ratio  # Brystningshøjde (0 for døre)
            opening_height = opening["height_mm"] / scale_ratio

            # Gør udskæringsboksen ekstra dyb (f.eks. 10 mm), så den helt sikkert skærer igennem væggen
            cut_depth = 10.0

            z_offset = (floor_thickness if include_floor else 0) + sill_height

            with BuildSketch(Plane.XY.offset(z_offset)):
                with Locations([(mid_x, mid_y)]):
                    Rectangle(width, cut_depth, rotation=angle_deg)

            # Mode.SUBTRACT trækker vindues-/dørvolumen fra de eksisterende vægge
            extrude(amount=opening_height, mode=Mode.SUBTRACT)

        # 3. TILFØJ EN SOLID BUNDPLADE (valgfri, men god til stueetage)
        if include_floor:
            bbox = building.part.bounding_box()
            floor_width = bbox.size.X
            floor_depth = bbox.size.Y
            center_x = (bbox.min.X + bbox.max.X) / 2.0
            center_y = (bbox.min.Y + bbox.max.Y) / 2.0

            with BuildSketch(Plane.XY):
                with Locations([(center_x, center_y)]):
                    Rectangle(floor_width, floor_depth)
            extrude(amount=floor_thickness)

    # 4. EKSPORTER TIL STL
    export_stl(building.part, output_filename)
    print(f"Færdig! 3D-model gemt som '{output_filename}' (Skala 1:{int(scale_ratio)})")


# =====================================================================
# EKSEMPEL PÅ INPUT-DATA FRA DIN FRONTEND (I virkelige millimeter)
# Et simpelt hus på 10 x 6 meter med en indvendig skillevæg, dør og vindue
# =====================================================================
if __name__ == "__main__":
    frontend_json_payload = {
        "wall_height_mm": 2500,  # 2,5 meter til loftet
        "walls": [
            # Ydervægge (350 mm tykke)
            {"start": [0, 0], "end": [10000, 0], "thickness_mm": 350},
            {"start": [10000, 0], "end": [10000, 6000], "thickness_mm": 350},
            {"start": [10000, 6000], "end": [0, 6000], "thickness_mm": 350},
            {"start": [0, 6000], "end": [0, 0], "thickness_mm": 350},
            # Indvendig skillevæg (kun 70 mm tyk -> bliver i 1:100 til 0.7 mm,
            # men scriptet hæver den automatisk til 1.2 mm for at kunne printes!)
            {"start": [4000, 0], "end": [4000, 6000], "thickness_mm": 70},
        ],
        "openings": [
            # Hoveddør i nederste ydervæg (bredde 1000 mm, højde 2100 mm, starter ved gulv)
            {"start": [1500, 0], "end": [2500, 0], "sill_height_mm": 0, "height_mm": 2100},
            # Stort stuevindue i nederste ydervæg (bredde 2000 mm, højde 1400 mm, 800 mm over gulv)
            {"start": [5500, 0], "end": [7500, 0], "sill_height_mm": 800, "height_mm": 1400},
            # Indvendig dør i skillevæggen
            {"start": [4000, 2500], "end": [4000, 3400], "sill_height_mm": 0, "height_mm": 2100},
        ],
    }

    # Kør genereringen i skala 1:100 (modellen bliver 100 x 60 mm på byggepladen)
    generate_3d_floorplan(
        plan_data=frontend_json_payload,
        scale_ratio=100.0,
        min_wall_mm=1.2,
        include_floor=True,
        output_filename="hus_1_til_100.stl",
    )
