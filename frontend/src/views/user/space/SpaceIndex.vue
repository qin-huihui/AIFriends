<script setup>
import {useRoute} from "vue-router";
// 取当前url信息
const route = useRoute()
// 打开新页面或者是后退
// const router = useRoute()



</script>

<template>
个人空间:{{route.params.user_id}}
</template>

<style scoped>

</style>