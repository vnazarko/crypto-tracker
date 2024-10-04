<script lang="ts" setup>
import { telegramLoginTemp } from 'vue3-telegram-login'

function yourCallbackFunction(user) {
    console.log(user);
    
}
</script>
<template>
    <div class="container">
        <header class="header">
            <h1 class="header_title">CryptoTrack</h1>
            <telegram-login-temp
                mode="callback"
                telegram-login="YourTelegramBot"
                @callback="yourCallbackFunction"
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