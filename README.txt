This is a testing cluster that tests:

1. Chef
2. Default runlist
3. jetpack download (blobs)
4. cluster-init scripts
5. cluster-init tests

To Use:

1. Deploy project as you normally would "cyclecloud project upload"
2. Create a cluster and use the UI to select the demo/default/1.0.0 spec
  - Note: No need to specify the runlist in your cluster template, the spec comes with one!
3. Set `cyclecloud.test_mode=true` in your cluster's configuration section (if you want to run the tests)
4. Start the cluster
  - Note: If you enabled tests, the converge will fail due to a testing error if the chef or cluster-init scripts did not produce the correct output!
