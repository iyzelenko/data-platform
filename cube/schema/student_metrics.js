cube(`StudentMetrics`, {
  sql: `SELECT * FROM student_events`,

  measures: {
    studentCount: {
      type: `count`
    },

    avgGrade: {
      sql: `grade`,
      type: `avg`
    }
  },

  dimensions: {
    faculty: {
      sql: `faculty`,
      type: `string`
    },

    student: {
      sql: `student`,
      type: `string`
    }
  }
});
