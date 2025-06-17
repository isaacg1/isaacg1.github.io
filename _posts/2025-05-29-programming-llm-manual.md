---
published: true
title: "Programming comparison: Manual and LLM"
layout: post
---

Let me put my cards on the table: I detest LLMs. I can't stand them and wish the structure of the universe was different so that they didn't work.

I detest their easy conflation of bullshit with substance,
the way they imperceptibly transition from outputting accurate information
for simple queries to outputting bullshit and falsehood
for slightly more complicated queries.
I detest their veneer of smarmy corporate bullshit,
reminiscent of SEO'd websites and marketing drones and empty suits.
I detest their economic model,
enormous capital costs and capital profits and centralized power and authority and control.
I reject them from the perspective of
[epistemic virtue](https://en.wikipedia.org/wiki/Epistemic_virtue)
and aesthetics and the well-being of people far and wide.

The last technology I detested with this fervor was NFTs.

I would be far happier in a world where LLMs don't work,
where they are not useful and effective.
Where they are just marketing hype and hot air.

I want to live in the world that actually exists.

I don't know what world I live in.

For a long time, I've seen LLM enthusiasts extol the virtues of LLMs,
but the quality was lacking.
They could generate general-purpose written text quickly,
but with much lower quality than would satisfy me,
rendering them only useful in situations where low-quality, low-effort text was desired,
or could be passed off as what was desired.
That didn't bother me too much.

Recently, I've heard LLM enthusiasts talk about its usefulness for programming.
In this case, these enthusiasts weren't claiming that LLMs were merely good
for writing throwaway code riddled with bugs that didn't do what one wanted it to do.
No, in this case these people were claiming that LLMs were an effective way
to write code more quickly and at the same quality as manual techniques.

And this wasn't just coming from people with something to sell:
this was coming from people I know and trust who have a history of accuracy.

So I have to try it out.
The epistemic virtue, the love of the truth, is what makes me detest LLMs,
and it is also what compels me to test them.

If LLMs work, if they provide a sizable speedup at producing something of quality,
I want to know that. If they don't work, I want to know that. 

The struggle against LLMs in a world where they work looks very different
than the struggle against LLMs in a world where they don't work.
I want to know what world I live in.

## Queueing simulator programming comparison

I program lots of simple queueing simulators for my research.
They're an important tool for understanding a theoretical queueing model.
They take a certain amount of time, nothing excessive but noticeable.

For my manual vs. LLM comparison, I'm programming a simple queueing simulator
from scratch in Rust. I have a fixed spec, with no flexibility.
I am targeting exact functional correctness, no bugs.

I am using a programming language that I am very comfortable with,
and a programming task that I am very comfortable with.
I think this is a fair comparison because the propensity of LLMs
to introduce bullshit means that they are not a good choice
if one cannot verify whether the outputted code is correct.

I am comparing my own manual programming with the GPT-4o LLM,
as it is easily accessible and free.
All of my manual tools are likewise free and easily accessible:
vim and the Rust compiler, and the std.rs and crates.io documentation.

I implemented the same spec once using each method.
The resulting programs, [manually written](#manual) and [written using an LLM](#llm), can be found at the end of this document.

I will evaluate these programs on five criteria:

* Correctness: Does the code correctly implement the spec,
including the programming-specific elements?
I'll keep going till it is correct, so this would only be a no if I gave up.
This is the most important quality.
* Time to implement: This is the alleged benefit of LLM-programming.
If it's correct and fast to write, that's major.
* Performance (runtime). This is important for my research,
as slow code will often take too long to reach convergence to be useful.
Also, runtime performance is correlated with code quality to a point:
code written simply and well will also often be efficient.
* Code quality: Is the code well-written?
Well written code is easier to read, understand, and extend.
* Degree of difficulty: was one test under easier or harder conditions?
* Emissions: LLMs have a reputation for causing lots of CO2 emissions.
I'll evaluate that.

## Specifications 

Create from scratch a closed, single-server queueing simulator.
There are always 10 jobs in the system - a new job is sampled whenever a job completes.
Job durations are uniformly distributed from 0 to 1, i.i.d. 

Performance measure: Amount by which response time exceeds a threshold of 5,
on average over all jobs. We'll call this metric the "mean exceedance".

Implement 3 scheduling policies:
- First-Come First-Served
- Shortest Processing Time
- Hybrid, where jobs which have been waiting for at least the threshold
  are prioritized and are served SPT, and other jobs are served FCFS.

Simulate each policy for 10 million jobs, then output the mean exceedence.

Programming spec:
The program must be written in Rust.
It should use the rand package (and optionally the rand_distr package)
to generate random values.
It should use the noisy_float package for float comparisons.


## Evaluation 

**Correctness:** Equal

Both programs gave identical outputs, to the sixth significant figure. I am confident in both programs' correctness. They each meet the spec, and each meet the programming spec.

**Time to implement**: Manual somewhat better

Manual: 15:01

LLM: 21:50

**Runtime Performance**: Manual better

Manual: 2.554s

LLM: 5.197s

**Code Quality**: Manual better

Manual:
* Better modularity
* Uses less powerful language methods, fit for what's needed.
* Generally simpler and easier to read.
* 81 lines
* [Clippy](https://doc.rust-lang.org/stable/clippy/index.html):
4 warnings, of which 2 matter.

LLM:
* Overcomplicated partition function 
* Policy match statement inline, rather than extracted to a method
* Parameters are global constants, not variables
* Job attributes are N64 when f64 would do.
* Completed jobs is a while loop when a for loop would do.
* Mapping to index is clunky
* Unnecessary mutability 
* 111 lines
* Clippy: 5 warnings, of which 3 matter.

**Degree of difficulty**: About equal

Manual:
Written while on the train, pausing to get on/off. 2 minutes on the platform, 6 minutes on the purple line, 7 minutes on the red line. The disrupted internet access would have made LLM-based programming more difficult.
Highly experienced, both in Rust and queueing simulator programming. 
Used only free tools.

LLM:
Stationary on the couch, uninterrupted. Previously wrote an essentially identical program as a test run. No other prior experience.
Used only free tools.

**Emissions**: Negligible

Research indicates that the LLaMa 65B LLM uses about
[4 Joules per output token](https://arxiv.org/abs/2310.03003).
The GPT 4o model I used is probably about 3 times bigger,
so let's say it uses about 12 Joules per output token.

In writing the LLM version of the program, I made 9 queries.
The overall transcript, including both inputs and outputs,
totalled about 4641 words and 39538 characters.
I don't know how a token corresponds to a word,
but I'll guess that 5000 tokens were output.

So writing this program used about 60,000 Joules of energy,
which is about 0.02 kWH.
That's an average of 55 Watts of power draw
over the 22 minute period, similar to a room's worth of lightbulbs.

Electricity in the US averages about
[0.81 pounds of CO2 per kWh](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11).
Writing this program lead to about 6 grams of CO2 emissions from LLM use.

For comparison, the average human exhales about 1kg of CO2 per day,
or about 0.7g of CO2 per minute.
As a result, I breathed out about 10 grams of CO2 while writing my program manually,
and about 15 grams while writing the LLM-based program.

These CO2 emissions are smaller than I care to track and optimize.

## Bugs (If I hadn't been an expert)

(Added after sharing the article with friends)

I specifically programmed something that I am an expert in.
What would have happened if I'd instead been programming something that I'm less familiar with?
It's hard to know for sure, but I can make some educated guesses,
based on the buggy intermediate versions that I received, during LLM programming.
I don't think that someone who wasn't an expert would've noticed these bugs,
or at the very least it would have taken much longer to find them.
Manual writing doesn't have as severe a problem in this regard, in my experience.
I think there would have been more bugs in the LLM version than if I was manually writing code I'm unfamiliar with,
and those bugs would've been more severe.

**Potential bugs:**

1. *Subtly different kind of queue*: Early versions of the code returned by the LLM implemented a subtly different kind of queue than I was looking for.
The early versions implemented system where, implicitly, all jobs were in service simultaneously, rather than the single-job-in-service that I was looking for.
This issue was mentioned by the LLM, offering a single-job-in-service version,
but only once I started reading through and correcting the code.
The LLM output also incorrectly claimed that in a closed queueing system, the default is for jobs to be processed in parallel (infinite server),
which is not an established default in my field. <br>
If I wasn't an expert, I might not have recognized the need to specify which type of queue I was looking for,
or recognized that I'd received the wrong one.

2. *Barely-correct code*: Early versions of the code returned by the LLM pretended to use `noisy_float` package that I told it use,
but actually avoided using that package while appearing to use it,
and instead used a different, bug-prone comparison method.
The problem that I was trying to solve is that rust does not have a built-in way to mark floats as "not NAN",
so ordering methods cannot be used with floats as keys by default.
The `noisy_float` package makes a "not NAN" float type available, solving this problem.
The returned code looks to the uninitiated like it's using this package, because it imports the package and wraps
the floats that need to be ordered in this type.
However, the code then extracted the underlying float from the N64 type, rendering the package pointless,
and then extracted the raw bit values of the float and sorted using those raw bit values.
This works in this specific case, giving the right output, but it's very delicate:
It treats negative values as larger than all positive values.
Thus, if my float comparison key had ever been negative,
the code would have been wrong.
This was essentially a bug waiting to happen.
The `noisy_float` package doesn't have this problem -- the nascent bug was introduced by the LLM code subtly avoiding my instructions. <br>
I don't think a non-expert would have caught this,
especially because the LLM also outputted framing text in which it claimed to be using the `noisy_float` package,
when in reality it had turned the use of that package into a no-op.

Also, while I was writing the code
I had thought that there'd been a bug involving treating a job duration as a job completion time,
but this was actually just that the LLM was outputting parallel-service code rather than one-job-at-a-time code.


## Conclusion 

Narrowly, manual programming is better. I took less time, produced better code, and had better runtime performance when I wrote it manually. The result of this test is clear: manual is better in all ways.

Broadly, LLM programming is close. There's probably people and situations where, if one doesn't share my disgust for LLMs, it might surpass manual programming. It is not just repeating code that already exists, it is a tool by which one can write general programs.

I implore you to reject LLMs if you possibly can. Its bullshit will forever be your downfall. It will erode your skills, pressure you to accede to the clarion call of shitty buggy code, and put more and more power in the hands of bigger and bigger corporations.

And for today at least, it's not even better. I hope it stays that way. Whether or not it does, I will live in the world that exists. I will see reality for what it really is. I'll try.

---

## Manually-written program {#manual}
`src/main.rs`:

```
use noisy_float::prelude::*;
use rand::prelude::*;

struct Job {
    arr_time: f64,
    duration: f64,
}

#[derive(Copy, Clone, Debug)]
enum Policy {
    FCFS,
    SPT,
    Hybrid,
}
impl Policy {
    fn serve(self, queue: &Vec<Job>, time: f64, threshold: f64) -> usize {
        match self {
            Policy::FCFS => 0,
            Policy::SPT => {
                queue
                    .iter()
                    .enumerate()
                    .min_by_key(|(_, job)| n64(job.duration))
                    .expect("job")
                    .0
            }
            Policy::Hybrid => {
                queue
                    .iter()
                    .enumerate()
                    .min_by_key(|(_, job)| {
                        if time - job.arr_time < threshold {
                            (1, n64(job.arr_time))
                        } else {
                            (0, n64(job.duration))
                        }
                    })
                    .expect("job")
                    .0
            }
        }
    }
}

fn sim(queue_size: usize, threshold: f64, num_jobs: u64, seed: u64, policy: Policy) -> f64 {
    let mut rng = StdRng::seed_from_u64(seed);
    let mut queue: Vec<Job> = (0..queue_size)
        .map(|_| Job {
            arr_time: 0.0,
            duration: rng.random_range(0.0..1.0),
        })
        .collect();
    let mut time = 0.0;
    let mut performance = 0.0;
    for _ in 0..num_jobs {
        let index = policy.serve(&queue, time, threshold);
        let job = queue.remove(index);
        time += job.duration;
        let response = time - job.arr_time;
        performance += (response - threshold).max(0.0);
        queue.push(Job {
            arr_time: time,
            duration: rng.random_range(0.0..1.0),
        })
    }
    performance / num_jobs as f64
}

fn main() {
    let queue_size = 10;
    let threshold = 5.0;
    let num_jobs = 10_000_000;
    let seed = 0;
    for policy in vec![Policy::FCFS, Policy::SPT, Policy::Hybrid] {
        let mean_performance = sim(queue_size, threshold, num_jobs, seed, policy);
        println!("{:?}: {}", policy, mean_performance);
    }
}
```

`Cargo.toml`:

```
[package]
name = "enby-test"
version = "0.1.0"
edition = "2024"

[dependencies]
noisy_float = "0.2.0"
rand = "0.9.1"
```

## Program written using LLM {#llm}

`src/main.rs`:

```
use noisy_float::types::N64;
use rand::prelude::*;
use rand_distr::Uniform;
use std::collections::VecDeque;

const NUM_JOBS: usize = 10_000_000;
const SYSTEM_SIZE: usize = 10;
const THRESHOLD: f64 = 5.0;

#[derive(Clone, Debug)]
struct Job {
    arrival_time: N64,
    duration: N64,
}

#[derive(Debug, Copy, Clone)]
enum Policy {
    FCFS,
    SPT,
    Hybrid,
}

fn run_simulation(policy: Policy) -> f64 {
    let mut rng = StdRng::seed_from_u64(0);
    let uniform = Uniform::new(0.0, 1.0).unwrap();

    let mut current_time = N64::new(0.0);
    let mut completed_jobs = 0usize;
    let mut total_excess = 0.0;

    let mut job_queue: VecDeque<Job> = VecDeque::new();

    // Seed initial jobs
    for _ in 0..SYSTEM_SIZE {
        let duration = N64::new(uniform.sample(&mut rng));
        let job = Job {
            arrival_time: current_time,
            duration,
        };
        job_queue.push_back(job);
    }

    while completed_jobs < NUM_JOBS {
        let job_index = match policy {
            Policy::FCFS => 0,
            Policy::SPT => job_queue
                .iter()
                .enumerate()
                .min_by_key(|(_, job)| job.duration)
                .map(|(i, _)| i)
                .unwrap(),
            Policy::Hybrid => {
                let (mut eligible, mut ineligible): (Vec<(usize, &Job)>, Vec<(usize, &Job)>) =
                    job_queue.iter().enumerate().partition(|(_, job)| {
                        (current_time - job.arrival_time) >= N64::new(THRESHOLD)
                    });

                if !eligible.is_empty() {
                    eligible
                        .into_iter()
                        .min_by_key(|(_, job)| job.duration)
                        .map(|(i, _)| i)
                        .unwrap()
                } else {
                    ineligible.first().map(|(i, _)| *i).unwrap()
                }
            }
        };

        let job = job_queue.remove(job_index).unwrap();

        let start_time = current_time;
        let completion_time = start_time + job.duration;
        let response_time = completion_time - job.arrival_time;
        let excess = (response_time.raw() - THRESHOLD).max(0.0);

        total_excess += excess;
        completed_jobs += 1;
        current_time = completion_time;

        // Add new job to keep system size constant
        let duration = N64::new(uniform.sample(&mut rng));
        let new_job = Job {
            arrival_time: current_time,
            duration,
        };
        job_queue.push_back(new_job);
    }

    total_excess / NUM_JOBS as f64
}

fn main() {
    let policies = [Policy::FCFS, Policy::SPT, Policy::Hybrid];

    for policy in policies {
        let name = match policy {
            Policy::FCFS => "FCFS",
            Policy::SPT => "SPT",
            Policy::Hybrid => "Hybrid",
        };

        let mean_excess = run_simulation(policy);
        println!(
            "{:<8} policy - Mean excess over threshold {:.1}: {:.6}",
            name, THRESHOLD, mean_excess
        );
    }
}
```

`Cargo.toml`:

```
[package]
name = "llm-test"
version = "0.1.0"
edition = "2024"

[dependencies]
noisy_float = "0.2.0"
rand = "0.9.1"
rand_distr = "0.5.1"
```
