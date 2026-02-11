<script setup>
import NavBar from "@/components/navbar/NavBar.vue";
</script>

<template>
<!-- 这个组件里面写html -->
  <NavBar>
    <!-- NavBar中的内容会直接填充到NavBar.vue中的slot组件中 -->
    <RouterView />
  </NavBar>
</template>

<style scoped>

</style>
