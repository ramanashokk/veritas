export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-white px-6">
      <h1 className="text-6xl font-bold tracking-tight text-black">
        VERITAS
      </h1>

      <p className="mt-3 text-xl text-gray-600">
        The Evidence Engine
      </p>

      <p className="mt-10 max-w-2xl text-center text-lg text-gray-700">
        What does the scientific evidence actually say?
      </p>

      <input
        type="text"
        placeholder="Ask a scientific question..."
        className="mt-8 w-full max-w-2xl rounded-xl border border-gray-300 px-5 py-4 text-lg outline-none focus:border-black"
      />

      <button className="mt-6 rounded-xl bg-black px-8 py-4 text-white transition hover:bg-gray-800">
        Verify
      </button>

      <p className="mt-16 text-sm text-gray-500">
        AI is not the authority. The evidence is.
      </p>
    </main>
  );
}