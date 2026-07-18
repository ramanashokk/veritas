'use client';

import { useState } from 'react';

type VerificationResponse = {
  claim: string;
  verification: {
    status: string;
    confidence: number;
  };
  consensus: {
    classification: string;
  };
  evidence: Array<{
    title: string;
    source: string;
    strength: string;
  }>;
};

export default function Home() {
  const [claim, setClaim] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<VerificationResponse | null>(null);

  async function handleVerify() {
    const trimmedClaim = claim.trim();

    if (!trimmedClaim) {
      setError('Please enter a scientific claim to verify.');
      setResult(null);
      return;
    }

    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/verify`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ claim: trimmedClaim }),
      });

      const payload = await response.json();

      if (!response.ok) {
        throw new Error(payload?.message || 'Verification failed.');
      }

      setResult(payload as VerificationResponse);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred.');
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-50 px-6 py-12 text-slate-900">
      <div className="mx-auto flex max-w-4xl flex-col gap-8">
        <header className="space-y-3">
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-slate-500">
            VERITAS
          </p>
          <h1 className="text-4xl font-semibold tracking-tight sm:text-5xl">
            Evidence-backed verification for scientific claims.
          </h1>
          <p className="max-w-2xl text-lg text-slate-600">
            Enter a scientific claim and review the structured verdict produced by the
            evidence pipeline.
          </p>
        </header>

        <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <label htmlFor="claim" className="mb-3 block text-sm font-medium text-slate-700">
            Scientific claim
          </label>
          <textarea
            id="claim"
            value={claim}
            onChange={(event) => setClaim(event.target.value)}
            placeholder="Example: COVID-19 vaccines reduce hospitalization."
            className="min-h-32 w-full rounded-xl border border-slate-300 px-4 py-3 text-base outline-none transition focus:border-slate-500"
          />

          <div className="mt-4 flex flex-wrap items-center gap-3">
            <button
              type="button"
              onClick={handleVerify}
              disabled={isLoading}
              className="rounded-xl bg-slate-900 px-5 py-3 font-medium text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:bg-slate-400"
            >
              {isLoading ? 'Verifying…' : 'Verify Claim'}
            </button>
            <p className="text-sm text-slate-500">
              Uses the FastAPI verification endpoint at /api/v1/verify.
            </p>
          </div>

          {error ? (
            <div className="mt-4 rounded-xl border border-rose-200 bg-rose-50 px-4 py-3 text-sm text-rose-700">
              {error}
            </div>
          ) : null}

          {!error && !isLoading && !result ? (
            <div className="mt-6 rounded-xl border border-dashed border-slate-200 bg-slate-50 px-4 py-6 text-sm text-slate-500">
              Enter a claim to begin verification.
            </div>
          ) : null}

          {isLoading ? (
            <div className="mt-6 rounded-xl border border-slate-200 bg-slate-50 px-4 py-6 text-sm text-slate-600">
              Gathering evidence and evaluating the claim…
            </div>
          ) : null}

          {result ? (
            <div className="mt-6 space-y-6">
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <h2 className="text-lg font-semibold">Verification result</h2>
                <dl className="mt-3 grid gap-4 sm:grid-cols-3">
                  <div>
                    <dt className="text-sm text-slate-500">Status</dt>
                    <dd className="mt-1 font-medium">{result.verification.status}</dd>
                  </div>
                  <div>
                    <dt className="text-sm text-slate-500">Confidence</dt>
                    <dd className="mt-1 font-medium">{result.verification.confidence.toFixed(2)}</dd>
                  </div>
                  <div>
                    <dt className="text-sm text-slate-500">Consensus</dt>
                    <dd className="mt-1 font-medium">{result.consensus.classification}</dd>
                  </div>
                </dl>
              </div>

              <div>
                <h3 className="text-lg font-semibold">Evidence</h3>
                <ul className="mt-3 space-y-3">
                  {result.evidence.map((item, index) => (
                    <li key={`${item.title}-${index}`} className="rounded-xl border border-slate-200 p-4">
                      <div className="flex items-start justify-between gap-4">
                        <div>
                          <p className="font-medium">{item.title}</p>
                          <p className="mt-1 text-sm text-slate-500">{item.source}</p>
                        </div>
                        <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium uppercase tracking-wide text-slate-600">
                          {item.strength}
                        </span>
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ) : null}
        </section>
      </div>
    </main>
  );
}