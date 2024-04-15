import { getCookie } from './Cookie'
import axios from 'axios'

export default axios.create({
    headers: {
        accessToken: getCookie('accessToken'),
    },
})