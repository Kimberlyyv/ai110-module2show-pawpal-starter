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

During this project, I used AI tools mainly to help with brainstorming the system design, writing the initial class skeletons, and debugging parts of the code. AI helped suggest how the classes like Owner, Pet, Task, and Scheduler should interact and how to organize the scheduling logic. I also used it when writing tests and improving parts of the code that handled sorting, filtering, and conflict detection.

The most helpful prompts were specific questions about how different parts of the system should connect. For example, asking how the Scheduler should retrieve tasks from the Owner’s pets or how to sort tasks by time helped me implement those features more clearly.

**b. Judgment and verification**

There were times when I did not accept AI suggestions exactly as they were given. For example, some suggestions added more complexity than I needed for this project. Instead of using those versions, I simplified the logic so it would still meet the requirements but remain easier to understand and maintain.

To verify the suggestions, I tested the code by running the demo script and the automated tests. If the output worked correctly and the tests passed, I knew the solution was working as intended.
---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, adding tasks to a pet, sorting tasks by time, recurring task creation, and conflict detection. These tests were important because they checked the main features of the system and helped confirm that the scheduler logic was working correctly.

**b. Confidence**

I am fairly confident that my scheduler works correctly for the main use cases I implemented. The tests helped verify that the system behaves as expected for important scheduling features. If I had more time, I would also test more edge cases, such as pets with no tasks, tasks with the same priority, and tasks that go over the owner’s available time.


---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
