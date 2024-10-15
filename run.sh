python evaluate.py \
  --task_name "scibench" \
  --file "thermo" \
  --propose_method "mistral" \
  --value_method "local" \
  --mode "mcts" \
  --evaluate "scibench" \
  --iteration_limit 50 \
  --use_reflection "simple" \
  --branch 3 > mcts.log 2>&1