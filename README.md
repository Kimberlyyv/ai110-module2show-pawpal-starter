# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt


### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

## Features

PawPal+ helps pet owners manage daily care tasks through a simple scheduling system.

Key features include:

- Add pets and store their information
- Create pet care tasks with duration and priority
- Sort tasks by scheduled time
- Filter tasks by completion status
- Detect scheduling conflicts between tasks
- Automatically create recurring tasks for daily or weekly activities
- Generate a daily schedule based on available time

## Testing PawPal+

To run the automated tests:

```bash
python -m pytest

##  Demo

Below is a screenshot of the PawPal+ Streamlit interface.

<a href="/course_images/ai110/pawpal_demo.png" target="_blank">
<img src='/course_images/ai110/pawpal_demo.png' title='PawPal App' alt='PawPal App' class='center-block' />
</a>

## System Architecture (UML)

![PawPal UML](uml_final.png)