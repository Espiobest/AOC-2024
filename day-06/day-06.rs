use rayon::prelude::*;
use std::fs;
use std::collections::HashSet;

const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)]; // N, E, S, W

fn path(start_x: usize, start_y: usize, grid: &Vec<Vec<char>>, part2: bool) -> Option<HashSet<(usize, usize)>> {
    let mut pos: HashSet<(usize, usize)> = HashSet::new();
    let mut visited: HashSet<(usize, usize, usize)> = HashSet::new();

    let mut nx: usize = start_x;
    let mut ny: usize = start_y;
    let mut dir: usize = 0;

    loop {
        if nx >= grid.len() || ny >= grid[0].len() {
            break;
        }

        if grid[nx][ny] != '#' {
            if part2 && visited.contains(&(nx, ny, dir)) {
                return None;
            }
            visited.insert((nx, ny, dir));
            pos.insert((nx, ny));
        }

        else {
            nx = (nx as i32 - DIRECTIONS[dir].0) as usize;
            ny = (ny as i32 - DIRECTIONS[dir].1) as usize;
            dir = (dir + 1) % 4;
        }

        nx = (nx as i32 + DIRECTIONS[dir].0) as usize;
        ny = (ny as i32 + DIRECTIONS[dir].1) as usize;
    }

    return Some(pos);
}

fn main() {
    let input: String = fs::read_to_string("day-06/data.txt").unwrap();
    let grid: Vec<Vec<char>> = input
    .lines()
    .map(|line| line.trim().chars().collect::<Vec<char>>())
    .collect();

    let mut start_x: usize = 0;
    let mut start_y: usize = 0;
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] == '^' {
                start_x = i;
                start_y = j;
            }
        }
    }

    let pos: HashSet<(usize, usize)> = path(start_x, start_y, &grid, false).unwrap();
    let part1: usize = pos.len();
    println!("Part 1: {}", part1);
    
    let part2: i32 = pos.par_iter()
    .filter_map(|(nx, ny)| {
        if *nx == start_x && *ny == start_y {
            return None;
        }

        let mut grid2: Vec<Vec<char>> = grid.clone();
        grid2[*nx][*ny] = '#';
        if path(start_x, start_y, &grid2, true).is_none() {
            return Some(1);
        }
        return Some(0);
    }).sum();

    println!("Part 2: {}", part2);
}

