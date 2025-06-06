'use client'

import Image from 'next/image'
import axios from 'axios'
import { useState } from 'react'
import APIResponse from '@/components/response'

export default function Home() {
  const [formData, setFormData] = useState({
    Pregnancies: '',
    Glucose: '',
    BloodPressure: '',
    SkinThickness: '',
    Insulin: '',
    BMI: '',
    DiabetesPedigreeFunction: '',
    Age: ''
  })
  const [response, setResponse] = useState('')

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/predict',
        formData
      )
      setResponse(response.data.prediction)
    } catch (error) {
      console.error('Error:', error)
      setResponse('Error')
    }
  }
  return (
    <main className="min-h-screen bg-gray-100 p-4 flex items-center justify-center flex-col">
      <Image
        src={'/sugar.png'}
        width={100}
        height={100}
        alt="Sugar image"
        className="m-5"
      ></Image>
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-md p-6">
        <h1 className="text-2xl font-bold mb-6 text-center">
          Diabetes Prediction
        </h1>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 sm:grid-cols-2 gap-4"
        >
          {Object.keys(formData).map(field => (
            <div key={field} className="flex flex-col">
              <label
                htmlFor={field}
                className="text-sm font-medium text-gray-700 mb-1"
              >
                {field}
              </label>
              <input
                type="number"
                id={field}
                name={field}
                value={formData[field as keyof typeof formData]}
                onChange={handleChange}
                className="p-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>
          ))}

          <div className="sm:col-span-2 mt-4">
            <button
              type="submit"
              className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700 transition-colors hover:cursor-pointer"
            >
              Submit
            </button>
          </div>
        </form>

        {response == '1' ? (
          <APIResponse text='You problaby have diabetes'></APIResponse>
        ) : response == '0' ? (
          <APIResponse text='You problaby do not have diabetes'></APIResponse>
        ) : null}
      </div>
    </main>
  )
}
