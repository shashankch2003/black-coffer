from langchain_openai import OpenAI

llm = OpenAI(temperature=0)

def generate_question(name):
    return f"Who is {name}?"

if __name__ == "__main__":
    while True:
        name = input("Enter a name (or type 'exit'): ")
        if name.lower() == "exit":
            break
        question = generate_question(name)
        answer = llm.invoke(question)
        print(f"\nQuestion: {question}\nAnswer: {answer}\n")
