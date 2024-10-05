<script lang="ts" setup>
import { telegramLoginTemp } from 'vue3-telegram-login'

function sendUserInfo(user) {
    console.log(user);
}
console.log(import.meta.env.VITE_API_URL);

</script>
<template>
    <div class="container">
        <header class="header">
            <h1 class="header_title">CryptoTrack</h1>
            <telegram-login-temp
                mode="callback"
                telegram-login="YourTelegramBot"
                @callback="sendUserInfo"
            />
        </header>
    </div>
</template>

<style lang="sass" scoped>
.header 
    width: 100%
    &_title 
        color: white
</style>