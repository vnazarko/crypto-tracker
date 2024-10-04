<script lang="ts" setup>
const testCallback = (user: any) => {
  console.log("Custom callback function: ",user);
};
</script>
<template>
    <header class="header">
        <h1 class="header_title">CryptoTrack</h1>
        <script async src="https://telegram.org/js/telegram-widget.js?22" data-telegram-login="CryptoTrackByNone1qqBot" data-size="medium" data-onauth="onTelegramAuth(user)" data-request-access="write" @click="testCallback(user)"></script>
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