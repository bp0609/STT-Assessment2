import subprocess
import time
import json

# Configuration combinations
worker_configs = [1, 'auto']
thread_configs = [1, 'auto']
dist_modes = ['load', 'no']

# Function to run the tests and record the results
def run_test(worker_count, thread_count, dist_mode, repetitions=3):
    results = []

    for _ in range(repetitions):
        command = [
            "pytest",
            f"--dist={dist_mode}",
            f"-n={worker_count}",
            f"--parallel-threads={thread_count}",
            "--maxfail=1",  # Stop after first failure (optional)
            "--disable-warnings",  # Disable warnings to keep output clean
            "--tb=short",  # Short traceback format
        ]

        print(f"Running pytest with {worker_count} workers, {thread_count} threads, and --dist={dist_mode}")

        # Run the command and time the execution
        start_time = time.time()
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()

        execution_time = end_time - start_time
        output = result.stdout

        # Parse output for test failures (failed tests are marked by "FAILED" in the output)
        failed_tests = []
        for line in output.splitlines():
            if "FAILED" in line:
                failed_tests.append(line)

        # Store results
        results.append({
            "worker_count": worker_count,
            "thread_count": thread_count,
            "dist_mode": dist_mode,
            "execution_time": execution_time,
            "failed_tests": failed_tests,
        })

        # Print results of the current run
        print(f"Execution time: {execution_time:.2f} seconds")
        if failed_tests:
            print(f"Failed tests: {failed_tests}")
        else:
            print("All tests passed!")

    return results

# Function to summarize the results (average execution time and flaky tests)
def summarize_results(results):
    summary = {}
    for result in results:
        key = (result['worker_count'], result['thread_count'], result['dist_mode'])
        if key not in summary:
            summary[key] = {
                'execution_times': [],
                'failed_tests': [],
            }

        summary[key]['execution_times'].append(result['execution_time'])
        summary[key]['failed_tests'].extend(result['failed_tests'])

    # Calculate average execution time and unique failed tests
    for key, value in summary.items():
        avg_execution_time = sum(value['execution_times']) / len(value['execution_times'])
        summary[key]['avg_execution_time'] = avg_execution_time
        summary[key]['unique_failed_tests'] = set(value['failed_tests'])

    return summary

# Main execution
def main():
    all_results = []

    # Test all combinations of workers, threads, and dist modes
    for worker_count in worker_configs:
        for thread_count in thread_configs:
            for dist_mode in dist_modes:
                results = run_test(worker_count, thread_count, dist_mode)
                all_results.extend(results)

    # Summarize the results
    summary = summarize_results(all_results)

    # Print the summary
    print("\nTest Execution Summary:")
    for (worker_count, thread_count, dist_mode), stats in summary.items():
        print(f"\nWorker Count: {worker_count}, Thread Count: {thread_count}, Dist Mode: {dist_mode}")
        print(f"Average Execution Time: {stats['avg_execution_time']:.2f} seconds")
        print(f"Unique Failed Tests: {len(stats['unique_failed_tests'])}")
        if stats['unique_failed_tests']:
            print(f"Failed Tests: {', '.join(stats['unique_failed_tests'])}")
        print("=" * 50)

if __name__ == "__main__":
    main()