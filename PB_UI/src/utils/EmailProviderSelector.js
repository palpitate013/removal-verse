import React, { useState } from 'react';
import Modal from './Modal';

const EMAIL_PROVIDERS = [
  { id: 'gmail', name: 'Gmail', logo: '📧' },
  { id: 'outlook', name: 'Outlook / Hotmail', logo: '📨' },
  { id: 'yahoo', name: 'Yahoo Mail', logo: '🔶' },
  { id: 'protonmail', name: 'ProtonMail', logo: '🔒' },
  { id: 'icloud', name: 'iCloud Mail', logo: '☁️' },
  { id: 'aol', name: 'AOL Mail', logo: '📬' },
  { id: 'mailru', name: 'Mail.ru', logo: '🇷🇺' },
  { id: 'yandex', name: 'Yandex Mail', logo: '🟡' },
  { id: 'zoho', name: 'Zoho Mail', logo: '📮' },
  { id: 'fastmail', name: 'FastMail', logo: '✉️' },
];

function EmailProviderSelector() {
  const [selectedProvider, setSelectedProvider] = useState(null);
  const [showModal, setShowModal] = useState(false);

  // Check if this is the first time the app is being used
  React.useEffect(() => {
    const hasSeenEmailProvider = localStorage.getItem('hasSeenEmailProvider');
    if (!hasSeenEmailProvider) {
      setShowModal(true);
    }
  }, []);

  const handleProviderSelect = (providerId) => {
    setSelectedProvider(providerId);
    // Store the selected provider
    localStorage.setItem('selectedEmailProvider', providerId);
    // Mark that the user has seen this modal
    localStorage.setItem('hasSeenEmailProvider', 'true');
    setShowModal(false);
  };

  return (
    <>
      {showModal && (
        <Modal>
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-gray-900 rounded-lg shadow-xl max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto border border-gray-700">
              <div className="p-8">
                <h2 className="text-3xl font-bold text-white mb-2">Select Your Email Provider</h2>
                <p className="text-gray-400 mb-8">
                  Which email provider do you use? This helps us tailor the service removal process for your account.
                </p>

                {/* Email Providers Grid */}
                <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mb-8">
                  {EMAIL_PROVIDERS.map((provider) => (
                    <button
                      key={provider.id}
                      onClick={() => handleProviderSelect(provider.id)}
                      className={`p-6 rounded-lg border-2 transition-all duration-200 flex flex-col items-center justify-center min-h-[140px] ${
                        selectedProvider === provider.id
                          ? 'border-blue-500 bg-blue-900 bg-opacity-20 text-white'
                          : 'border-gray-600 bg-gray-800 hover:border-gray-500 hover:bg-gray-750 text-gray-300'
                      }`}
                    >
                      <span className="text-4xl mb-3">{provider.logo}</span>
                      <span className="text-sm font-medium text-center">{provider.name}</span>
                    </button>
                  ))}
                </div>

                {/* Action Buttons */}
                <div className="flex gap-4 justify-end">
                  <button
                    onClick={() => {
                      localStorage.setItem('hasSeenEmailProvider', 'true');
                      setShowModal(false);
                    }}
                    className="px-6 py-2 rounded-lg border border-gray-600 text-gray-300 hover:text-white hover:border-gray-500 transition-colors"
                  >
                    Skip for Now
                  </button>
                  <button
                    onClick={() => selectedProvider && handleProviderSelect(selectedProvider)}
                    disabled={!selectedProvider}
                    className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                      selectedProvider
                        ? 'bg-blue-600 text-white hover:bg-blue-700'
                        : 'bg-gray-600 text-gray-400 cursor-not-allowed'
                    }`}
                  >
                    Continue
                  </button>
                </div>
              </div>
            </div>
          </div>
        </Modal>
      )}
    </>
  );
}

export default EmailProviderSelector;
