import klayout.db as db
# import klayout.lib as lib_basic
import numpy as np
import os
import klayout.lib

lib_basic = db.Library.library_by_name("Basic")
ly = db.Layout()
# sets unit to micrometer
LY_DBU = ly.dbu


class Polygon:
    '''
    abstract class
    '''
    def __init__(self, name: str, polygon, centered=True):
        self.name = name
        self.centered = centered
        self.polygon = polygon

    def transformation(self, dx, dy, rotation=0, magnitude=1, mirrorx=False):
        complex_transformation = db.ICplxTrans(magnitude, rotation, mirrorx, int(dx / LY_DBU), int(dy / LY_DBU))
        self.polygon.transform(complex_transformation)


class Rectangle(Polygon):
    def __init__(self, name: str, x: float, y: float, centered=True):
        self.x = x
        self.y = y
        self.centered = centered

        x_um = self.x / LY_DBU
        y_um = self.y / LY_DBU
        if self.centered:
            point_rectangle = [db.DPoint(-x_um / 2, -y_um / 2), db.DPoint(x_um / 2, -y_um / 2),
                               db.DPoint(x_um / 2, y_um / 2), db.DPoint(-x_um / 2, y_um / 2)]
        else:
            point_rectangle = [db.DPoint(0, 0), db.DPoint(x_um, 0), db.DPoint(x_um, y_um), db.DPoint(0, y_um)]

        self.polygon = db.Polygon(point_rectangle)
        super().__init__(name, self.polygon, centered)


class Circle(Polygon):

    def __init__(self, name: str, radius: float, centered=True, nr_points=64):
        self.radius = radius
        self.nr_points = nr_points

        radius = self.radius / LY_DBU
        angles = np.linspace(0, 2 * np.pi, self.nr_points + 1)[0:-1]
        points = []  # array of points
        for angle in angles:
            points.append(db.Point(radius * np.cos(angle), radius * np.sin(angle)))
        self.polygon = db.Polygon(points)
        super().__init__(name, self.polygon, centered)


class Region:
    def __init__(self, polygon_object_list):
        len(polygon_object_list)
        self.polygon_list = [polygon_object.polygon for polygon_object in polygon_object_list]
        self.region = db.Region(self.polygon_list)

    def subtract(self, region_to_subtract):
        return self.region - region_to_subtract.region

    def add(self, region_to_add):
        return self.region + region_to_add.region


class Cell:
    # doc string
    def __init__(self, name: str):
        self.name = name
        self.layers = {}  # dict with layers as keys
        self.cell = ly.create_cell(self.name)

    def draw_polygon(self, polygon_object, target_layer):
        self.cell.shapes(target_layer).insert(polygon_object.polygon)
        #it would be nice if we could add multiple polygons at the same time/to multiple layers at the same time

    def draw_path(self, path_object, target_layer):
        self.cell.shapes(target_layer).insert(path_object.path)

    def draw_region(self, region_polygon, target_layer):
        self.cell.shapes(target_layer).insert(region_polygon)

    def insert_cell(self, cell_to_insert, origin_x=0, origin_y=0, magnitude=1, rotation=0, mirrorx=False):
        complex_transformation = db.ICplxTrans(magnitude, rotation, mirrorx, int(origin_x / LY_DBU),
                                               int(origin_y / LY_DBU))
        cell_instance = db.CellInstArray(cell_to_insert.cell.cell_index(), complex_transformation)
        self.cell.insert(cell_instance)

    def insert_cell_array(self, cell_to_insert, x_row, y_row, x_column, y_column, n_row: int, n_column: int,
                          origin_x=0, origin_y=0, magnitude=1, rotation=0, mirrorx=False):
        v_row = db.Vector(x_row / LY_DBU, y_row / LY_DBU)
        v_column = db.Vector(x_column / LY_DBU, y_column / LY_DBU)
        complex_transformation = db.ICplxTrans(magnitude, rotation, mirrorx, int(origin_x / LY_DBU),
                                               int(origin_y / LY_DBU))
        cell_instance_array = db.CellInstArray(cell_to_insert.cell.cell_index(), complex_transformation, v_row,
                                               v_column, n_row, n_column)
        self.cell.insert(cell_instance_array)

    def flatten(self):
        self.cell.flatten(-1, True)


class Path:
    def __init__(self, points: list, width: float):
        self.points = points
        self.width = width
        self.path = db.Path([point/LY_DBU for point in self.points], self.width/LY_DBU)
#
# class Text(Cell):
#
#
