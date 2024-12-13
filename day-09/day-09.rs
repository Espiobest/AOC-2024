use std::fs::File;
use std::io::{self, Read};
use std::vec;

fn main() -> io::Result<()> {
    // Read the file
    let mut file = File::open("data.txt")?;
    let mut nums = String::new();
    file.read_to_string(&mut nums)?;

    // Part 1 and Part 2 processing
    let (part1, part2) = process_file(&nums);

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);

    Ok(())
}

fn process_file(nums: &str) -> (usize, usize) {
    let mut data = Vec::new();
    let mut dots = Vec::new();
    let mut cur_id = 0;

    // First pass: populate data and dots
    for (i, ch) in nums.chars().enumerate() {
        let num = ch.to_digit(10).unwrap() as usize;
        if i % 2 == 0 {
            // File IDs
            data.extend(std::iter::repeat(cur_id).take(num));
            cur_id += 1;
        } else {
            // Dot placeholders
            let start = data.len();
            data.extend(std::iter::repeat('.').take(num));
            dots.extend(start..data.len());
        }
    }

    // Part 1 processing
    let mut data_part1 = data.clone();
    for idx in dots.iter() {
        if *idx >= data_part1.len() {
            break;
        }
        let val = data_part1.pop().unwrap();
        data_part1[*idx] = val;
    }

    // Trim trailing dots
    while let Some('.') = data_part1.last() {
        data_part1.pop();
    }

    let part1 = data_part1.iter().enumerate()
        .map(|(i, &e)| if e == '.' { 0 } else { i * e })
        .sum();

    // Part 2 processing
    let mut data_part2 = data.clone();
    let mut dot_groups = Vec::new();

    // Identify dot groups
    for (i, &item) in data_part2.iter().enumerate() {
        if item == '.' {
            if i == 0 || data_part2[i - 1] != '.' {
                dot_groups.push(vec![i]);
            } else {
                dot_groups.last_mut().unwrap().push(i);
            }
        }
    }

    // Identify file data
    let mut file_data = Vec::new();
    let mut i = 0;
    while i < data_part2.len() {
        if data_part2[i] != '.' {
            let file_id = data_part2[i];
            let start = i;
            while i < data_part2.len() && data_part2[i] == file_id {
                i += 1;
            }
            let size = i - start;
            file_data.push((file_id, size, start));
        } else {
            i += 1;
        }
    }
    file_data.reverse();

    // Place files
    for (file_id, size, start_index) in file_data {
        for (j, dots) in dot_groups.iter_mut().enumerate() {
            if dots.len() >= size && dots[0] < start_index {
                for k in 0..size {
                    data_part2[dots[k]] = file_id;
                    data_part2[start_index + k] = '.';
                }
                *dots = dots[size..].to_vec();
                if dots.is_empty() {
                    dot_groups.remove(j);
                }
                break;
            }
        }
    }

    // Calculate part 2
    let part2 = data_part2.iter().enumerate()
        .map(|(i, &e)| if e == '.' { 0 } else { i * e })
        .sum();

    (part1, part2)
}