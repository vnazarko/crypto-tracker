<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'

onMounted(() => {
  localStorage.setItem('coin', '1');
  localStorage.setItem('currency', 'USD');
  localStorage.setItem('stock-market', 'Binance');
})
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>
