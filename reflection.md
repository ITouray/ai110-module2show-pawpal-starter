# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
entering owner and pet information 
adding and editing pet care tasks
generating a daily care schedule. 
Each action maps to a distinct layer of the system 

- What classes did you include, and what responsibilities did you assign to each?

A user should be able to perform three core actions in the app:

- Add or edit pet care tasks, including details like task name, duration, and priority.
- Enter owner and pet information such as owner name, pet name, and species.
- Generate and view a daily care schedule for today, showing which tasks should happen and when.

The main objects for the system are:

- `Owner`: holds owner name and preferences; can provide availability and preference data.
- `Pet`: holds pet name, species, and basic pet info; can describe pet needs and context.
- `Task`: holds a task title, duration, priority, and optional notes; can determine whether it is a high-priority or time-sensitive task.
- `Scheduler` or `Plan`: holds a list of tasks and scheduling constraints; can generate a daily plan, order tasks, and explain the reasoning behind the chosen schedule.

**b. Design changes**

- Did your design change during implementation?
Yes.
- If yes, describe at least one change and why you made it.
Added completed: bool to Task: requires users to add and edit tasks, but the original Task had no way to track whether a task had been completed. Without this field, the scheduler can't distinguish pending from done tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
Time budget, task priority, completion status, scheduled start time, and recurrence frequency.

- How did you decide which constraints mattered most?
Missing medication or feeding has real health consequences. Time is crucial, you can't do more than the budget allows. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
detect_conflicts() to flags tasks that share the exact same time.

- Why is that tradeoff reasonable for this scenario?
Making exact-match detection sufficient for the real mistake an owner would make.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
Create and update Mermaid.live diagram, generating class and method stubs, and drafting tests.

- What kinds of prompts or questions were most helpful?
Detailed prompts

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
I rejected AI's suggestion for updating UML design. 

- How did you evaluate or verify what the AI suggested?
Reading thru it and making sure AI suggestions agligns with my design, rather than just copy + paste.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
Behavious I tested includes: Priority ordering, time budget enforcement, completed-task exclusion, daily and weekly recurrence, conflict detection, and chronological sorting.

- Why were these tests important?
They're important because  a wrong priority order, missed budget check, or bad recurrence date could cause a pet owner to miss medication or feeding with no visible error.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I don't have any pets, but if I had any I would use this app to care for my pet.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
Turn this web app into a phone app.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
There are so many ways to design the same app. And having a good design is essential for getting a good app.
