interface propsAPIResponse {
  text: string
}

export default function APIResponse({ text }: propsAPIResponse) {
  return (
    <div className="flex justify-center items-center text-center p-4">
      <p className="font-bold text-3xl">{text}</p>
    </div>
  )
}
