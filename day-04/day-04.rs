use::std;

fn main() {
    let input: String = std::fs::read_to_string("day-04/data.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect::<Vec<&str>>();

    let mut part1: usize = 0;

    // horizontal check
    lines.iter().for_each(|line| {
        part1 += line.matches("XMAS").count() + line.matches("SAMX").count();
    });

    // vertical check
    for col in 0..lines[0].len() {
        let mut line: String = String::new();
        for row in &lines {
            line.push(row.chars().nth(col).unwrap());
        }
        part1 += line.matches("XMAS").count() + line.matches("SAMX").count();
    }

    // diagonal check
    for i in 0..(lines.len() - 3) {
        for j in 0..(lines[0].len() - 3) {
            let main: String = (0..4).map(|k| lines[i+k].chars().nth(j+k).unwrap()).collect();
            let off: String = (0..4).map(|k| lines[i+k].chars().nth(j+3-k).unwrap()).collect();
            part1 += main.matches("XMAS").count() + main.matches("SAMX").count();
            part1 += off.matches("XMAS").count() + off.matches("SAMX").count();
        }
    }

    println!("Part 1: {}", part1);

    let mut part2: usize = 0;
    for i in 0..(lines.len() - 2) {
        for j in 0..(lines[0].len() - 2) {
            let main: String = (0..3).map(|k| lines[i+k].chars().nth(j+k).unwrap()).collect();
            let off: String = (0..3).map(|k| lines[i+k].chars().nth(j+2-k).unwrap()).collect();
            if main == "MAS" || main == "SAM" {
                part2 += off.matches("MAS").count() + off.matches("SAM").count();
            }
        }
    }
    
    println!("Part 2: {}", part2);
    
    
}