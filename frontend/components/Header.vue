<script lang="ts" setup>
const testCallback = (user: any) => {
  console.log("Custom callback function: ",user);
};

onMounted(() => {
    const script = document.createElement('script');
    script.src = 'https://telegram.org/js/telegram-widget.js?22';
    script.setAttribute('data-telegram-login', 'CryptoTrackByNone1qqBot');
    script.setAttribute('data-size', 'medium');
    script.setAttribute('data-onauth', 'testCallback(user)');
    script.setAttribute('data-request-access', 'write');
    document.getElementById('telegram-button').appendChild(script);
})
</script>
<template>
    <header class="header">
        <h1 class="header_title">CryptoTrack</h1>
    </header>
    <div class="header_telegram-button" id="telegram-button"></div>
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