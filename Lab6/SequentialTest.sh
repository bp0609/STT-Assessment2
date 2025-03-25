# Part (a): Sequential Test Execution
# -------------------------------

NUM_SEQ_RUNS=10
STABLE_RUNS=3

# echo "=== Sequential Test Execution: Initial 10 Runs ==="
> seq_run_logs/sequential_timings.log
> seq_run_logs/sequential_failures.log

# for run in $(seq 1 $NUM_SEQ_RUNS); do
#     echo "Sequential Run #$run"
#     start_time=$(date +%s.%N)
#     # Run the test suite sequentially (without parallel options)
#     pytest > "seq_run_logs/seq_run_${run}.log" 2>&1
#     exit_code=$?
#     end_time=$(date +%s.%N)
#     duration=$(echo "$end_time - $start_time" | bc)
#     echo "Run #$run duration: $duration seconds" | tee -a seq_run_logs/sequential_timings.log

#     if [ $exit_code -ne 0 ]; then
#         echo "Run #$run encountered failures. See seq_run_${run}.log for details." | tee -a seq_run_logs/sequential_failures.log
#     fi
# done

# echo ""
# echo "Please review 'sequential_failures.log' to eliminate failing/flaky tests."
# echo "Once the test suite is stable, proceed with the next phase."

# (Pause for manual intervention; user should fix the tests before continuing.)
# read -p "Press [Enter] to continue with stable sequential runs..."
sleep 5
echo ""
echo "=== Sequential Test Execution: Stable Runs (for Tseq) ==="
> seq_run_logs/stable_timings.log

total_time=0
for run in $(seq 1 $STABLE_RUNS); do
    echo "Stable Sequential Run #$run"
    start_time=$(date +%s.%N)
    pytest > "seq_run_logs/stable_run_${run}.log" 2>&1
    end_time=$(date +%s.%N)
    duration=$(echo "$end_time - $start_time" | bc)
    total_time=$(echo "$total_time + $duration" | bc)
    echo "Stable Run #$run duration: $duration seconds" | tee -a seq_run_logs/stable_timings.log
done

# Calculate average Tseq from stable runs
Tseq=$(echo "scale=4; $total_time / $STABLE_RUNS" | bc)
echo "Average sequential execution time (Tseq): $Tseq seconds"