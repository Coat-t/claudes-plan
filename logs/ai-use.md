# **Ai usage and logs**
|Date|Names|Tools|Purpose|
|-|-|-|-|
|23.10.2026|Mukha|Claude|To decorate the main Markdown file with special headings, tables, formatting etc.|
|23.10.2026|Mukha|Claude|Get suggestions for roles for team members according to their strengths and background|
|24.10.2026|Hasnat|Deepseek|Beginner friendly analogies for the topic|
|24.10.2026|Wasi|ChatGPT|Basic information and concepts for the topic|
|24.10.2026|Liyi|Deepseek|Generate material for writing the substantive content of a coherent topic|
|24.10.2026|Mukha|Claude (Claude Code)|Compare the four Stage 1 checklists with the repository and list the gaps (review only)|
|24.10.2026|Mukha|Claude (Claude Code)|Move the README master task list into GitHub Issues #7-#33 and the project board|
|25.10.2026|Mukha|Claude (Claude Code)|Check the failed Task 2 submission (10/30) against the requirements, restructure the repository, and build the resubmission package and reports|

|Names|Prompts|Checks|
|-|-|-|
|Mukha|Apply special headings, tables, and text formats, to the information given, in markdown language|Checking design and readability|
|Hasnat|Give key concepts of subtopics for beginners to easily understand it and make things clear in their mind|Grammer check, simpler language|
|Wasi| Analyze the information given about the project and inform me about potential risks|fact check|
|Liyi| Generate a summary containing History, development, purpose and impact of Ai, as wel as other materials|Grammer check, source check, fact check|
|Mukha|"read .todo.md and compare to the github repo"|Mukha decided to use AI only for pointing out gaps: "I can't use AI too much because it will be bad for the usage records"|
|Mukha|"could you quickly move all the tasks from README's Master task list into Github project? ..."|Claude created the issues and set the board statuses to match the README; the README tables were then replaced by a link (commit bdab938)|
|Mukha|"check and complete task 2, it already has a failed attempt" and "also create a Resubmission Report file, covering what was wrong and what changes were made"|Claude compared Liyi's text word by word before and after the move (wording unchanged) and checked the WEF jobs figure against the WEF press release. Mukha still has to review the branch diff and the PDFs before resubmitting.|

## **Outcome :**
- Mukha used the information from ai, to help him delegate roles and assign tasks to the members, as well as decorating the general format of the readme.
- Hasnat wrote the subtopic content with the help of the Ai.
- Wasi used ai to analyze current state of the project to find potential risks.
- Liyi sourced contents of this topic from the material given by Ai.
- Mukha used Claude to move Liyi's content into `content/`, build the module outline from the README, export the task list from GitHub, fix Markdown formatting, store the diagram locally, and draft the Task 2 submission and resubmission reports. Claude did not write new learning content. The problems it found are listed in `content/00-module-outline.md` under Gaps and uncertainties.
- The 23.10.2026 Claude sessions did more than formatting. Mukha wrote the member, strength and responsibility lines, the target learners and the first five topics. Claude drafted the Collaboration and Workload section, widened the roles on request, added five topics, and wrote the scope boundaries, the planned learning resources and mini lecture, the schedule and the master task list. Commit 0eb056f contains that draft unchanged. The full record, with prompts and outputs, is R1 in the Stage 1 project log.
