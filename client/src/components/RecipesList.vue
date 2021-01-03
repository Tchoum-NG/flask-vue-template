<template>
  <div>
    {{ recipes }}
  </div>
</template>

<script>
import axios from 'axios';
export default {

  data: function() {
    return {
      recipes: []
    }
  },

  created() {
    this.getData();
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/readall';
      axios.get(path)
        .then((res) => {
          this.recipes = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
}
</script>