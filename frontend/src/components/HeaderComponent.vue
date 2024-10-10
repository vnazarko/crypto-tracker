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
                'photo_url': user.photo_url,
                'active': true
            }
        )
        .then((res) => {
            console.log(res)
        })
        .catch((error) => {
            if (error.response.status == 400) {
                login(user.id, user.hash)
                
            }
        })
}


function login(id, hash) {
    const form = new FormData();
    form.append('id', id);
    form.append('hash', hash);

    axios.post(`https://${import.meta.env.VITE_API_URL}/auth/login`, form, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }).then((res) => {
        localStorage.setItem('access_token', res.data.access_token);
        localStorage.setItem('refresh_token', res.data.refresh_token);
        
    }).catch((error) => {
        console.log(error);
        
    });
}


function authFunc(method, url, callback) {
    let access_token = localStorage.getItem('access_token');
    let refresh_token = localStorage.getItem('refresh_token');

    if (!access_token) {
        axios.post(`https://${import.meta.env.VITE_API_URL}/auth/refresh`, null, {
                    headers: {
                        'Authorization': `Bearer ${refresh_token}`
                    }
                })
            .then((res) => {
                access_token = res.data.access_token;
                localStorage.setItem('access_token', access_token);
                
                axios.get(`https://${import.meta.env.VITE_API_URL}${url}`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('refresh_token')}`
                    }
                }).then((res) => {
                    callback(res);
                }).catch((err) => {
                    console.log(err);
                })
            });
    } else {
        axios({
            method: method,
            url: `https://${import.meta.env.VITE_API_URL}${url}`,
            headers: {
                Authorization: `Bearer ${access_token}`
            }
        }).then((res) => {
            callback(res);
        }).catch((err) => {
            if (err.response.status === 401) {
                axios.post(`https://${import.meta.env.VITE_API_URL}/auth/refresh`, null, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('refresh_token')}`
                    }
                })
                    .then((res) => {
                        access_token = res.data.access_token;
                        localStorage.setItem('access_token', access_token);
                        axios({
                            method: method,
                            url: `https://${import.meta.env.VITE_API_URL}${url}`,
                            headers: {
                                'Authorization': `Bearer ${access_token}`
                            }
                        }).then((res) => {
                            callback(res);
                        }).catch((err) => {
                            console.log(err);
                        });
                    });
            } else {
                console.log(err);
            }
        })
    }
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
    height: 90px
    display: flex 
    justify-content: space-between
    align-items: center
    border-bottom: solid 1px rgba(1, 101, 56, 0.4)
    &_title 
        color: #EFFDF5
        font-size: 30px
        font-family: DM_Sans
        font-weight: 700 
        text-align: center 

</style>