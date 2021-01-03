<template>
  <v-navigation-drawer
    :value="drawer"
    class="elevation-4"
    color="blue lighten-4"  
  >
    <v-list-item>
      <v-text-field
        class="pt-4"
        label="Solo"
        placeholder="Rechercher"
        solo
      />
    </v-list-item>
  </v-navigation-drawer>
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