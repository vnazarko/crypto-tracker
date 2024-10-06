<script lang="ts" setup>
import { telegramLoginTemp } from 'vue3-telegram-login'
import axios from 'axios'

function sendUserInfo(user) {
    axios
        .post(
            `https://${import.meta.env.VITE_API_URL}/auth/register`, 
            {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                ''
            }
        )
        .then((res) => {
            console.log(res)
        })
        .catch((error) => {
            console.error(error)
        })
}

</script>
<template>
    <div class="container">
        <header class="header">
            <h1 class="header_title">CryptoTrack</h1>
            <telegram-login-temp
                mode="callback"
                telegram-login="CryptoTrackByNone1qqBot"
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