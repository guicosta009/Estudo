/*
  Parametric 3D auditorium inspired by the supplied seating plan.

  Units are millimetres.  Render in OpenSCAD with F6, then export STL/3MF,
  or use the command from the README for a command-line export.
*/

$fn = 20;

// Overall shell
room_width = 42000;
room_depth = 30000;
wall_height = 6000;
wall_thickness = 300;

// Seating layout: 11 banks, each containing a 3-seat bench, by 8 rows.
bank_count = 11;
row_count = 8;
seats_per_bank = 3;
seat_pitch = 650;
bank_pitch = 3550;
row_pitch = 1900;
front_clearance = 5000;
side_margin = (room_width - bank_count * bank_pitch) / 2;

module box(size, position = [0, 0, 0], colour = [0.7, 0.7, 0.7]) {
    color(colour) translate(position) cube(size);
}

module chair() {
    // A simple fixed auditorium chair: pedestal, cushion, back and arm rests.
    box([80, 80, 430], [285, 240, 0], [0.10, 0.12, 0.14]);
    box([500, 480, 110], [75, 40, 430], [0.10, 0.36, 0.48]);
    box([500, 85, 530], [75, 420, 470], [0.08, 0.28, 0.38]);
    box([55, 390, 55], [15, 80, 570], [0.07, 0.09, 0.10]);
    box([55, 390, 55], [580, 80, 570], [0.07, 0.09, 0.10]);
}

module seating_bank() {
    // Platform makes every group readable even in a simple exported model.
    box([seats_per_bank * seat_pitch + 160, 680, 100], [0, 0, 0], [0.12, 0.16, 0.18]);
    for (seat = [0 : seats_per_bank - 1])
        translate([80 + seat * seat_pitch, 80, 100]) chair();
}

module table() {
    box([1400, 700, 80], [-700, -350, 790], [0.55, 0.42, 0.25]);
    for (x = [-600, 500]) for (y = [-250, 150])
        box([70, 70, 760], [x, y, 30], [0.20, 0.16, 0.10]);
}

module speaker() {
    box([700, 300, 1250], [0, 0, 0], [0.06, 0.06, 0.07]);
    color([0.18, 0.18, 0.18]) translate([350, -5, 650]) rotate([90, 0, 0])
        cylinder(h = 20, r = 150);
}

module stage() {
    // Raised platform at the rear of the room, with a backdrop and presentation screen.
    box([room_width - 2 * wall_thickness, 2800, 450], [wall_thickness, room_depth - 3200, 0], [0.20, 0.20, 0.23]);
    box([room_width - 2 * wall_thickness, 180, 3600], [wall_thickness, room_depth - 450, 450], [0.13, 0.14, 0.16]);
    box([7200, 90, 2200], [(room_width - 7200) / 2, room_depth - 560, 1500], [0.88, 0.88, 0.84]);
    translate([room_width / 2, room_depth - 1800, 450]) table();
    for (x = [-1600, 1600])
        translate([room_width / 2 + x - 325, room_depth - 2500, 450]) chair();
    translate([1500, room_depth - 1900, 450]) speaker();
    translate([room_width - 2200, room_depth - 1900, 450]) speaker();
}

module room_shell() {
    color([0.78, 0.78, 0.74, 0.35]) difference() {
        cube([room_width, room_depth, wall_height]);
        translate([wall_thickness, wall_thickness, 0])
            cube([room_width - 2 * wall_thickness, room_depth - 2 * wall_thickness, wall_height + 1]);
        // Entrance opening centered on the front wall.
        translate([room_width / 2 - 1800, -1, 0]) cube([3600, wall_thickness + 2, 2600]);
    }
    box([room_width - 2 * wall_thickness, room_depth - 2 * wall_thickness, 80],
        [wall_thickness, wall_thickness, 0], [0.18, 0.20, 0.19]);
}

room_shell();
stage();

// Seating faces the stage (+Y).  The aisle between banks follows the source plan.
for (row = [0 : row_count - 1])
    for (bank = [0 : bank_count - 1])
        translate([side_margin + bank * bank_pitch,
                   front_clearance + row * row_pitch, 80])
            seating_bank();

// A low front divider and two entrance-side columns complete the basic room massing.
box([room_width, 120, 1000], [0, 3600, 0], [0.30, 0.31, 0.30]);
box([1000, 1000, 3000], [0, 0, 0], [0.22, 0.23, 0.22]);
box([1000, 1000, 3000], [room_width - 1000, 0, 0], [0.22, 0.23, 0.22]);
