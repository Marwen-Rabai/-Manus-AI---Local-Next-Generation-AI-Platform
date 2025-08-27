def log_message(message: str) -> None:
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def save_results(results: dict, filename: str) -> None:
    """Saves the results to a specified file."""
    with open(filename, 'w') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")