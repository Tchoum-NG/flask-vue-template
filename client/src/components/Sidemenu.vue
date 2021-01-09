<template>
  <div>
  </div>
</template>

<script>
export default{
  computed: {
    drawer(){
      return this.$store.getters.getSidebar;
    }
  }
}
</script>