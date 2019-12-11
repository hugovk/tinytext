module.exports = function(grunt) {
  var srcFiles = ["**/*.py"];

  // Project configuration.
  grunt.initConfig({
    flake8: {
      options: {
        // Task-specific options go here.
        spawn: false
      },
      src: srcFiles
    },

    exec: {
      run_tests:
        "coverage run --source=tinytext tests/test_tinytext.py && coverage report"
    },

    watch: {
      files: srcFiles,
      tasks: ["exec", "flake8"]
    }
  });

  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-exec");
  grunt.loadNpmTasks("grunt-flake8");

  grunt.registerTask("default", ["watch"]);
};
