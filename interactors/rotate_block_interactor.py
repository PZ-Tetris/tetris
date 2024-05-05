from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class RotateBlockInteractor():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard

    def rotate_block(self, block: Block):
        print('rotate')
        """Rotate the block 90 degrees clockwise if possible"""
        block_ids = block.block_ids
        center_x = sum(self.canvas.coords(block_id)[0] for block_id in block_ids) / len(block_ids)
        center_y = sum(self.canvas.coords(block_id)[1] for block_id in block_ids) / len(block_ids)

        # Przechowujemy nowe współrzędne po obrocie dla każdego bloku
        new_coords = []

        # Oblicz nowe współrzędne po obrocie dla każdego bloku
        for block_id in block_ids:
            x1, y1, x2, y2 = self.canvas.coords(block_id)
            new_x1 = center_x - (y2 - center_y) + 25
            new_y1 = center_y + (x1 - center_x)
            new_x2 = center_x - (y1 - center_y) + 25
            new_y2 = center_y + (x2 - center_x)
            new_coords.append((new_x1, new_y1, new_x2, new_y2))

        # Sprawdź, czy nowe współrzędne po obrocie mieszczą się na planszy
        all_within_bounds = all(
            0 <= new_x1 <= self.canvas.winfo_width() and
            0 <= new_x2 <= self.canvas.winfo_width() and
            0 <= new_y1 <= self.canvas.winfo_height() and
            0 <= new_y2 <= self.canvas.winfo_height()
            for new_x1, new_y1, new_x2, new_y2 in new_coords
        )

        # Jeśli wszystkie bloki klocka mieszczą się na planszy po obrocie, wykonaj rotację
        if all_within_bounds:
            for block_id, (new_x1, new_y1, new_x2, new_y2) in zip(block_ids, new_coords):
                self.canvas.coords(block_id, new_x1, new_y1, new_x2, new_y2)