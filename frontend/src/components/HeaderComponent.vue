<script lang="ts" setup>
import {vueTelegramLogin} from 'vue-telegram-login'

function yourCallbackFunction(user) {
    console.log(user);
    
}
</script>
<template>
    <div class="container">
        <header class="header">
            <vue-telegram-login 
                mode="callback"
                telegram-login="CryptoTrackByNone1qqBot"
                @callback="yourCallbackFunction" />
        </header>
    </div>
</template>

<style lang="sass" scoped>

</style>