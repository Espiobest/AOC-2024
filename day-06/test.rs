use std::fs;
use std::collections::{HashSet, HashMap};

const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)]; // N, E, S, W

// Function to simulate the guard's movement and check if they form a loop
fn path(start_x: usize, start_y: usize, grid: &Vec<Vec<char>>, part2: bool) -> Option<HashSet<(usize, usize)>> {
    let mut pos: HashSet<(usize, usize)> = HashSet::new();
    let mut visited: HashSet<(usize, usize, usize)> = HashSet::new();  // (x, y, direction)

    let mut nx: usize = start_x;
    let mut ny: usize = start_y;
    let mut dir: usize = 0;

    loop {
        if nx >= grid.len() || ny >= grid[0].len() {
            break;
        }

        if grid[nx][ny] != '#' {
            if part2 && visited.contains(&(nx, ny, dir)) {
                return None;  // Loop detected
            }
            visited.insert((nx, ny, dir));  // Mark this position with its direction
            pos.insert((nx, ny));
        }

        // When encountering an obstacle, change direction
        if grid[nx][ny] == '#' {
            nx = (nx as i32 - DIRECTIONS[dir].0) as usize;
            ny = (ny as i32 - DIRECTIONS[dir].1) as usize;
            dir = (dir + 1) % 4;
        } else {
            nx = (nx as i32 + DIRECTIONS[dir].0) as usize;
            ny = (ny as i32 + DIRECTIONS[dir].1) as usize;
        }
    }

    Some(pos)
}

fn main() {
    let input: String = fs::read_to_string("day-06/data.txt").unwrap();
    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.trim().chars().collect::<Vec<char>>())
        .collect();

    let mut start_x: usize = 0;
    let mut start_y: usize = 0;

    // Find the initial position of the guard
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] == '^' {
                start_x = i;
                start_y = j;
            }
        }
    }

    // Part 1: Find the visited positions
    let pos: HashSet<(usize, usize)> = path(start_x, start_y, &grid, false).unwrap();
    let part1: usize = pos.len();
    println!("Part 1: {}", part1);

    // Part 2: Try adding obstacles and see if it causes a loop
    let mut part2: i32 = 0;

    for (nx, ny) in pos {
        if nx == start_x && ny == start_y {
            continue;  // Skip the guard's starting position
        }

        let mut grid2: Vec<Vec<char>> = grid.clone();
        grid2[nx][ny] = '#';  // Place an obstacle

        // Check if adding this obstacle causes a loop
        if path(start_x, start_y, &grid2, true).is_none() {
            part2 += 1;
        }

        println!("Obstacle at: ({}, {})", nx, ny);  // For debugging purposes
    }

    println!("Part 2: {}", part2);
}
