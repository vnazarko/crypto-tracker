<script lang="ts" setup>
const testCallback = (user: any) => {
  console.log("Custom callback function: ",user);
};
</script>
<template>
    <header class="header">
        <h1 class="header_title">CryptoTrack</h1>
        <TelegramLoginWidget telegram-login="my_bot" @callback="testCallback" />
    </header>
</template>

<style lang="sass" scoped>
.header 
    height: 82px
    display: flex 
    align-items: center 
    justify-content: center 
    border-bottom: 1px solid rgba(1, 101, 56, 0.4)
    &_title
        font-size: 30px
        font-weight: 700 
        text-align: center
</style>