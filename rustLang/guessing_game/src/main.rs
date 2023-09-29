use rand::Rng;
use std::cmp::Ordering;
use std::io;


fn main() {
    println!("The Number Guessing Game!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    //println!("The secret number is: {secret_number}");

    let mut counter = 1;
    
    loop {

        if counter == 1 {
            println!("Take a guess!");
        }
        else {
            println!("Try again.");
        }
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Sorry, too low!"),
            Ordering::Greater => println!("Oops, too high!"),
            Ordering::Equal => {
                println!("Oh yeah! You won!");
                break;
            }
        }

        counter = counter+1;
    }
}