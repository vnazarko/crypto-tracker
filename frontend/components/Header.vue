<script setup>
// const route = useRoute()

// watch(() => route, (newRoute) => {
//   console.log('track route: ', newRoute)
// }, { immediate: true, deep: true })

// onMounted(() => {
//     const script = document.createElement('script');
//     script.src = 'https://telegram.org/js/telegram-widget.js?22';
//     script.setAttribute('data-telegram-login', 'CryptoTrackByNone1qqBot');
//     script.setAttribute('data-size', 'large');
//     script.setAttribute('data-auth-url', 'https://crypto-track.none1qq.ru/');
//     script.setAttribute('data-request-access', 'write');
//     document.getElementById('telegram-button').appendChild(script);
// })

function telegramLoadedCallbackFunc() {
    console.log('Telegram user loaded')
}
function yourCallbackFunction(user) {
    console.log(user)
}
</script>
<template>
    <header class="header">
        <h1 class="header_title">CryptoTrack</h1>
        <telegram-login-temp
            mode="callback"
            telegram-login="YourTelegramBot"
            @loaded='telegramLoadedCallbackFunc'
            @callback="yourCallbackFunction"
        />
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