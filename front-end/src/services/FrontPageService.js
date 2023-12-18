import axios from "axios"


export const SendLoadData = async (files) => {
    const chunkSize = 100;
    const numberOfChunks = Math.ceil(files.length / chunkSize);
    for (let i = 0; i < numberOfChunks; i++) {
        const start = i * chunkSize;
        const end = (i + 1) * chunkSize;
        const chunk = files.slice(start, end);
        const formData = new FormData();
        for (let j = 0; j < chunk.length; j++) {
            formData.append(`file${j + 1}`, chunk[j]);
        }
        try{
            const response = await axios.post(`${process.env.REACT_APP_PYTHON_APP_API_URL}/api/LoadData`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
            });
            console.log(response);
        }catch(err){
            console.log(err);
        }
    }
}

export const SendWeatherData = async (files) => {
    const formData = new FormData();
    for(let i = 0; i < files.length; i++){
        formData.append(`file${i + 1}`, files[i]);
    }
    return await axios.post(`${process.env.REACT_APP_PYTHON_APP_API_URL}/api/WeatherData`, formData, 
    {
        headers: {
            'Content-Type' : 'multipart/form-data'
        },
    });
}

export const SendUSHolidaysData = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return await axios.post(`${process.env.REACT_APP_PYTHON_APP_API_URL}/api/USHolidaysData`, formData, 
    {
        headers: {
            'Content-Type' : 'multipart/form-data'
        },
    });
}

export const TrainModel = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}

export const BeginForecast = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}