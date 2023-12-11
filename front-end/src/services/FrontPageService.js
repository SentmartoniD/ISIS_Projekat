import axios from "axios"

export const Pelda = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}

export const SendLoadData = async (files) => {
    
}

export const SendWeatherData = async (files) => {
    
}

export const SendUSHolidaysData = async (file) => {
    
}

export const TrainModel = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}

export const BeginForecast = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}