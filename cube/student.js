cube(`Students`, {
  sql: `SELECT * FROM students`,

  measures: {
    count: {
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
    }
  }
});