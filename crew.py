from crewai import Crew
from agents import flaky_test_detector, root_cause_analyst, fix_recommender
from tasks import detect_flaky_tests, analyze_root_cause, recommend_fixes





def build_crew():
    detector = flaky_test_detector()
    analyst = root_cause_analyst()
    recommender = fix_recommender()

    task1 = detect_flaky_tests(detector)
    task2 = analyze_root_cause(analyst)
    task3 = recommend_fixes(recommender)

    # Context chaining
    task2.context = [task1]
    task3.context = [task2]

    crew = Crew(
        agents=[detector, analyst, recommender],
        tasks=[task1, task2, task3],
        verbose=True,
    )

    return crew


if __name__ == "__main__":
    import json
    crew = build_crew()
    result = crew.kickoff()
    
    # Save the structured output to a JSON file at the project level
    if result.json_dict:
        with open("final_report.json", "w") as f:
            json.dump(result.json_dict, f, indent=2)
        print("\n✅ Final structured report saved to final_report.json")
    else:
        print("\n⚠️ No JSON data returned from the crew.")
    
    print("\n--- Final Result Object ---")
    print(result)