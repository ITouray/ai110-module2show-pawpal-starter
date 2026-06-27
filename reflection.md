# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
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
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
