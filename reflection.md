# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. Each class has a specific role in the system.

The Owner class represents the pet owner and stores their pets. It allows the owner to add pets and access tasks for all pets.

The Pet class represents each pet and stores information like the pet’s name and type. It also keeps a list of tasks that belong to that pet.

The Task class represents a single pet care activity, like feeding or walking. It includes details such as the task description, duration, priority, and whether the task has been completed.

The Scheduler class is responsible for organizing tasks and generating a daily plan. It collects tasks from all pets and helps sort or organize them into a schedule.

**b. Design changes**

During implementation, I made a small change to the design. At first, I kept the Task class more basic, but later I added a frequency attribute so tasks could better represent repeated pet care activities like feeding or walking. I also decided that the Scheduler class should handle organizing tasks across all pets instead of having each Pet do that on its own.

These changes made the system more practical and kept the responsibilities of each class clearer.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

You can write it like this:

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler mainly considers task time, completion status, available time, and task priority**. It uses task time to sort the schedule in order, checks completion status so finished tasks are not added again, and uses the owner’s available time to make sure the daily plan is realistic. I also included priority as an important part of the task information so the system can keep track of which tasks matter more.

I decided these constraints mattered most because they matched the main goal of the project, which is helping a busy pet owner stay organized and complete important pet care tasks in a reasonable schedule. I wanted the scheduler to stay simple but still be practical, so I focused on the constraints that would have the biggest impact on planning a day.

**b. Tradeoffs**

One tradeoff my scheduler makes is that it only checks for exact time conflicts instead of more detailed overlapping task durations. I think this is reasonable for this project because it keeps the logic simple while still helping the user notice obvious scheduling problems.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
