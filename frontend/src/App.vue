<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'

onMounted(() => {
  localStorage.setItem('coin', 'BTC');
  localStorage.setItem('currency', 'USD');
  localStorage.setItem('stockMarket', 'Binance');
})
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>
