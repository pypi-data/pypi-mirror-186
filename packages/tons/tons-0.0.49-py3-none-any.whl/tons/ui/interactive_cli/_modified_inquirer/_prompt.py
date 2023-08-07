def modified_prompt(questions, render, answers=None, raise_keyboard_interrupt=False):
    answers = answers or {}
    questions_num = len(questions)

    try:
        for idx, question in enumerate(questions):
            answers[question.name] = render.render(question, idx, questions_num, answers)
        return answers
    except KeyboardInterrupt:
        if raise_keyboard_interrupt:
            raise
        print("")
        print("Cancelled by user")
        print("")
