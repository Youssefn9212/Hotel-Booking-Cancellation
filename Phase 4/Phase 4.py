{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "1214c321",
      "metadata": {
        "id": "1214c321"
      },
      "source": [
        "# Data Cleaning\n",
        "Youssef Nakhla 900201430\n",
        "Karim AbouDaoud 900212779\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Uv67mTDuIjr",
        "outputId": "3465bfe5-55f2-495a-ef13-447324745e64"
      },
      "id": "5Uv67mTDuIjr",
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "7ec02d2c",
      "metadata": {
        "id": "7ec02d2c"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import plotly.express as px\n",
        "import plotly.graph_objects as go\n",
        "import scipy.stats\n",
        "import plotly.figure_factory as ff\n",
        "import seaborn as sns\n",
        "from scipy.stats import f_oneway\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.preprocessing import MinMaxScaler"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "id": "35317c64",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 342
        },
        "id": "35317c64",
        "outputId": "93d4fcb2-9847-4c9f-c65e-08ae2b454abf"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
              "0  Resort Hotel            0        342               2015               July   \n",
              "1  Resort Hotel            0        737               2015               July   \n",
              "2  Resort Hotel            0          7               2015               July   \n",
              "3  Resort Hotel            0         13               2015               July   \n",
              "4  Resort Hotel            0         14               2015               July   \n",
              "\n",
              "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
              "0                        27                          1   \n",
              "1                        27                          1   \n",
              "2                        27                          1   \n",
              "3                        27                          1   \n",
              "4                        27                          1   \n",
              "\n",
              "   stays_in_weekend_nights  stays_in_week_nights  adults  ...  deposit_type  \\\n",
              "0                        0                     0       2  ...    No Deposit   \n",
              "1                        0                     0       2  ...    No Deposit   \n",
              "2                        0                     1       1  ...    No Deposit   \n",
              "3                        0                     1       1  ...    No Deposit   \n",
              "4                        0                     2       2  ...    No Deposit   \n",
              "\n",
              "   agent company days_in_waiting_list customer_type   adr  \\\n",
              "0    NaN     NaN                    0     Transient   0.0   \n",
              "1    NaN     NaN                    0     Transient   0.0   \n",
              "2    NaN     NaN                    0     Transient  75.0   \n",
              "3  304.0     NaN                    0     Transient  75.0   \n",
              "4  240.0     NaN                    0     Transient  98.0   \n",
              "\n",
              "   required_car_parking_spaces  total_of_special_requests  reservation_status  \\\n",
              "0                            0                          0           Check-Out   \n",
              "1                            0                          0           Check-Out   \n",
              "2                            0                          0           Check-Out   \n",
              "3                            0                          0           Check-Out   \n",
              "4                            0                          1           Check-Out   \n",
              "\n",
              "  reservation_status_date  \n",
              "0              01/07/2015  \n",
              "1              01/07/2015  \n",
              "2              02/07/2015  \n",
              "3              02/07/2015  \n",
              "4              03/07/2015  \n",
              "\n",
              "[5 rows x 32 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-899e6e1f-4f2c-4e85-87c9-f0d95bf2e36a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>hotel</th>\n",
              "      <th>is_canceled</th>\n",
              "      <th>lead_time</th>\n",
              "      <th>arrival_date_year</th>\n",
              "      <th>arrival_date_month</th>\n",
              "      <th>arrival_date_week_number</th>\n",
              "      <th>arrival_date_day_of_month</th>\n",
              "      <th>stays_in_weekend_nights</th>\n",
              "      <th>stays_in_week_nights</th>\n",
              "      <th>adults</th>\n",
              "      <th>...</th>\n",
              "      <th>deposit_type</th>\n",
              "      <th>agent</th>\n",
              "      <th>company</th>\n",
              "      <th>days_in_waiting_list</th>\n",
              "      <th>customer_type</th>\n",
              "      <th>adr</th>\n",
              "      <th>required_car_parking_spaces</th>\n",
              "      <th>total_of_special_requests</th>\n",
              "      <th>reservation_status</th>\n",
              "      <th>reservation_status_date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Resort Hotel</td>\n",
              "      <td>0</td>\n",
              "      <td>342</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>01/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Resort Hotel</td>\n",
              "      <td>0</td>\n",
              "      <td>737</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>01/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Resort Hotel</td>\n",
              "      <td>0</td>\n",
              "      <td>7</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>...</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>75.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>02/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Resort Hotel</td>\n",
              "      <td>0</td>\n",
              "      <td>13</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>...</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>304.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>75.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>02/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Resort Hotel</td>\n",
              "      <td>0</td>\n",
              "      <td>14</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>240.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>98.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>03/07/2015</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 32 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-899e6e1f-4f2c-4e85-87c9-f0d95bf2e36a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-899e6e1f-4f2c-4e85-87c9-f0d95bf2e36a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-899e6e1f-4f2c-4e85-87c9-f0d95bf2e36a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-a50a5b96-564a-4c05-b6e4-f7b1379db35d\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-a50a5b96-564a-4c05-b6e4-f7b1379db35d')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-a50a5b96-564a-4c05-b6e4-f7b1379db35d button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "df=pd.read_csv(\"/content/drive/MyDrive/hotel_bookings.csv\")\n",
        "df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "55510f4a",
      "metadata": {
        "id": "55510f4a"
      },
      "source": [
        "# Checking For NA's"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "id": "9ff5c814",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9ff5c814",
        "outputId": "e7193a0a-627b-4cad-d1dd-5d52d37e78fc"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "hotel                                  0\n",
              "is_canceled                            0\n",
              "lead_time                              0\n",
              "arrival_date_year                      0\n",
              "arrival_date_month                     0\n",
              "arrival_date_week_number               0\n",
              "arrival_date_day_of_month              0\n",
              "stays_in_weekend_nights                0\n",
              "stays_in_week_nights                   0\n",
              "adults                                 0\n",
              "children                               4\n",
              "babies                                 0\n",
              "meal                                   0\n",
              "country                              488\n",
              "market_segment                         0\n",
              "distribution_channel                   0\n",
              "is_repeated_guest                      0\n",
              "previous_cancellations                 0\n",
              "previous_bookings_not_canceled         0\n",
              "reserved_room_type                     0\n",
              "assigned_room_type                     0\n",
              "booking_changes                        0\n",
              "deposit_type                           0\n",
              "agent                              16340\n",
              "company                           112593\n",
              "days_in_waiting_list                   0\n",
              "customer_type                          0\n",
              "adr                                    0\n",
              "required_car_parking_spaces            0\n",
              "total_of_special_requests              0\n",
              "reservation_status                     0\n",
              "reservation_status_date                0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "df.isnull().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "id": "6f7f156d",
      "metadata": {
        "id": "6f7f156d"
      },
      "outputs": [],
      "source": [
        "#dropping 4 NAs of variable children\n",
        "df.dropna(subset=[\"children\"],inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "3c25366a",
      "metadata": {
        "id": "3c25366a"
      },
      "outputs": [],
      "source": [
        "#94% of company is missing so it will be dropped\n",
        "df=df.drop([\"company\"],axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"agent\"].fillna(0, inplace=True)"
      ],
      "metadata": {
        "id": "9odA0uQFuBTG"
      },
      "id": "9odA0uQFuBTG",
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "id": "dead3a3f",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dead3a3f",
        "outputId": "8833736e-91df-42a5-814f-7cdcb774e6f6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "country\n",
              "PRT    48586\n",
              "GBR    12129\n",
              "FRA    10415\n",
              "ESP     8568\n",
              "DEU     7287\n",
              "       ...  \n",
              "DJI        1\n",
              "BWA        1\n",
              "HND        1\n",
              "VGB        1\n",
              "NAM        1\n",
              "Name: count, Length: 177, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ],
      "source": [
        "df[\"country\"].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "id": "e9502f10",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e9502f10",
        "outputId": "99986783-8e61-41f2-cbf8-f7a32a8f3488"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "488"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ],
      "source": [
        "df[\"country\"].isnull().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "id": "40e1b681",
      "metadata": {
        "id": "40e1b681"
      },
      "outputs": [],
      "source": [
        "df[\"country\"].fillna(df[\"country\"].mode()[0], inplace=True) #filling NAs with the most frequent values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "id": "b9f0308e",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b9f0308e",
        "outputId": "0bcc5726-1b9b-4cbc-9cf7-e452839d5749"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "hotel                             0\n",
              "is_canceled                       0\n",
              "lead_time                         0\n",
              "arrival_date_year                 0\n",
              "arrival_date_month                0\n",
              "arrival_date_week_number          0\n",
              "arrival_date_day_of_month         0\n",
              "stays_in_weekend_nights           0\n",
              "stays_in_week_nights              0\n",
              "adults                            0\n",
              "children                          0\n",
              "babies                            0\n",
              "meal                              0\n",
              "country                           0\n",
              "market_segment                    0\n",
              "distribution_channel              0\n",
              "is_repeated_guest                 0\n",
              "previous_cancellations            0\n",
              "previous_bookings_not_canceled    0\n",
              "reserved_room_type                0\n",
              "assigned_room_type                0\n",
              "booking_changes                   0\n",
              "deposit_type                      0\n",
              "agent                             0\n",
              "days_in_waiting_list              0\n",
              "customer_type                     0\n",
              "adr                               0\n",
              "required_car_parking_spaces       0\n",
              "total_of_special_requests         0\n",
              "reservation_status                0\n",
              "reservation_status_date           0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ],
      "source": [
        "df.isnull().sum()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SxUSGQ2evE60",
        "outputId": "4c3ee5a3-f0d5-4cb8-bbfa-4f65cebfc597"
      },
      "id": "SxUSGQ2evE60",
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',\n",
              "       'arrival_date_month', 'arrival_date_week_number',\n",
              "       'arrival_date_day_of_month', 'stays_in_weekend_nights',\n",
              "       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',\n",
              "       'country', 'market_segment', 'distribution_channel',\n",
              "       'is_repeated_guest', 'previous_cancellations',\n",
              "       'previous_bookings_not_canceled', 'reserved_room_type',\n",
              "       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',\n",
              "       'days_in_waiting_list', 'customer_type', 'adr',\n",
              "       'required_car_parking_spaces', 'total_of_special_requests',\n",
              "       'reservation_status', 'reservation_status_date'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f20a8e14",
      "metadata": {
        "id": "f20a8e14"
      },
      "source": [
        "# Hotel"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "id": "de72d57b",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "de72d57b",
        "outputId": "98ea5bb3-c5a0-4291-a479-77148e1dea63"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Resort Hotel', 'City Hotel'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ],
      "source": [
        "class_names = df[\"hotel\"].unique()\n",
        "class_names"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "id": "f74ea1c4",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 444
        },
        "id": "f74ea1c4",
        "outputId": "192b4dbe-74be-44e0-b3ec-d4a5b194d97f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
              "0          0            0        342               2015               July   \n",
              "1          0            0        737               2015               July   \n",
              "2          0            0          7               2015               July   \n",
              "3          0            0         13               2015               July   \n",
              "4          0            0         14               2015               July   \n",
              "...      ...          ...        ...                ...                ...   \n",
              "119385     1            0         23               2017             August   \n",
              "119386     1            0        102               2017             August   \n",
              "119387     1            0         34               2017             August   \n",
              "119388     1            0        109               2017             August   \n",
              "119389     1            0        205               2017             August   \n",
              "\n",
              "        arrival_date_week_number  arrival_date_day_of_month  \\\n",
              "0                             27                          1   \n",
              "1                             27                          1   \n",
              "2                             27                          1   \n",
              "3                             27                          1   \n",
              "4                             27                          1   \n",
              "...                          ...                        ...   \n",
              "119385                        35                         30   \n",
              "119386                        35                         31   \n",
              "119387                        35                         31   \n",
              "119388                        35                         31   \n",
              "119389                        35                         29   \n",
              "\n",
              "        stays_in_weekend_nights  stays_in_week_nights  adults  ...  \\\n",
              "0                             0                     0       2  ...   \n",
              "1                             0                     0       2  ...   \n",
              "2                             0                     1       1  ...   \n",
              "3                             0                     1       1  ...   \n",
              "4                             0                     2       2  ...   \n",
              "...                         ...                   ...     ...  ...   \n",
              "119385                        2                     5       2  ...   \n",
              "119386                        2                     5       3  ...   \n",
              "119387                        2                     5       2  ...   \n",
              "119388                        2                     5       2  ...   \n",
              "119389                        2                     7       2  ...   \n",
              "\n",
              "        booking_changes  deposit_type  agent days_in_waiting_list  \\\n",
              "0                     3    No Deposit    0.0                    0   \n",
              "1                     4    No Deposit    0.0                    0   \n",
              "2                     0    No Deposit    0.0                    0   \n",
              "3                     0    No Deposit  304.0                    0   \n",
              "4                     0    No Deposit  240.0                    0   \n",
              "...                 ...           ...    ...                  ...   \n",
              "119385                0    No Deposit  394.0                    0   \n",
              "119386                0    No Deposit    9.0                    0   \n",
              "119387                0    No Deposit    9.0                    0   \n",
              "119388                0    No Deposit   89.0                    0   \n",
              "119389                0    No Deposit    9.0                    0   \n",
              "\n",
              "       customer_type     adr  required_car_parking_spaces  \\\n",
              "0          Transient    0.00                            0   \n",
              "1          Transient    0.00                            0   \n",
              "2          Transient   75.00                            0   \n",
              "3          Transient   75.00                            0   \n",
              "4          Transient   98.00                            0   \n",
              "...              ...     ...                          ...   \n",
              "119385     Transient   96.14                            0   \n",
              "119386     Transient  225.43                            0   \n",
              "119387     Transient  157.71                            0   \n",
              "119388     Transient  104.40                            0   \n",
              "119389     Transient  151.20                            0   \n",
              "\n",
              "        total_of_special_requests  reservation_status reservation_status_date  \n",
              "0                               0           Check-Out              01/07/2015  \n",
              "1                               0           Check-Out              01/07/2015  \n",
              "2                               0           Check-Out              02/07/2015  \n",
              "3                               0           Check-Out              02/07/2015  \n",
              "4                               1           Check-Out              03/07/2015  \n",
              "...                           ...                 ...                     ...  \n",
              "119385                          0           Check-Out              06/09/2017  \n",
              "119386                          2           Check-Out              07/09/2017  \n",
              "119387                          4           Check-Out              07/09/2017  \n",
              "119388                          0           Check-Out              07/09/2017  \n",
              "119389                          2           Check-Out              07/09/2017  \n",
              "\n",
              "[119386 rows x 31 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4dcf3106-a0d9-43b7-9118-2eb1f67d9b78\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>hotel</th>\n",
              "      <th>is_canceled</th>\n",
              "      <th>lead_time</th>\n",
              "      <th>arrival_date_year</th>\n",
              "      <th>arrival_date_month</th>\n",
              "      <th>arrival_date_week_number</th>\n",
              "      <th>arrival_date_day_of_month</th>\n",
              "      <th>stays_in_weekend_nights</th>\n",
              "      <th>stays_in_week_nights</th>\n",
              "      <th>adults</th>\n",
              "      <th>...</th>\n",
              "      <th>booking_changes</th>\n",
              "      <th>deposit_type</th>\n",
              "      <th>agent</th>\n",
              "      <th>days_in_waiting_list</th>\n",
              "      <th>customer_type</th>\n",
              "      <th>adr</th>\n",
              "      <th>required_car_parking_spaces</th>\n",
              "      <th>total_of_special_requests</th>\n",
              "      <th>reservation_status</th>\n",
              "      <th>reservation_status_date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>342</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>3</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>01/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>737</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>4</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>01/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>75.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>02/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>13</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>304.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>75.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>02/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>14</td>\n",
              "      <td>2015</td>\n",
              "      <td>July</td>\n",
              "      <td>27</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>240.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>98.00</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>03/07/2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>119385</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>23</td>\n",
              "      <td>2017</td>\n",
              "      <td>August</td>\n",
              "      <td>35</td>\n",
              "      <td>30</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>394.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>96.14</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>06/09/2017</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>119386</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>102</td>\n",
              "      <td>2017</td>\n",
              "      <td>August</td>\n",
              "      <td>35</td>\n",
              "      <td>31</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>9.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>225.43</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>07/09/2017</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>119387</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>34</td>\n",
              "      <td>2017</td>\n",
              "      <td>August</td>\n",
              "      <td>35</td>\n",
              "      <td>31</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>9.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>157.71</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>07/09/2017</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>119388</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>109</td>\n",
              "      <td>2017</td>\n",
              "      <td>August</td>\n",
              "      <td>35</td>\n",
              "      <td>31</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>89.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>104.40</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>07/09/2017</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>119389</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>205</td>\n",
              "      <td>2017</td>\n",
              "      <td>August</td>\n",
              "      <td>35</td>\n",
              "      <td>29</td>\n",
              "      <td>2</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>No Deposit</td>\n",
              "      <td>9.0</td>\n",
              "      <td>0</td>\n",
              "      <td>Transient</td>\n",
              "      <td>151.20</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Check-Out</td>\n",
              "      <td>07/09/2017</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>119386 rows × 31 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4dcf3106-a0d9-43b7-9118-2eb1f67d9b78')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4dcf3106-a0d9-43b7-9118-2eb1f67d9b78 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4dcf3106-a0d9-43b7-9118-2eb1f67d9b78');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-d42d184f-2878-4a11-bfc1-1602a087fece\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-d42d184f-2878-4a11-bfc1-1602a087fece')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-d42d184f-2878-4a11-bfc1-1602a087fece button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ],
      "source": [
        "df.loc[ df[\"hotel\"] == class_names[0],\"hotel\"]=0 #resort =0\n",
        "df.loc[ df[\"hotel\"] == class_names[1],\"hotel\"]=1 #city =1\n",
        "df"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "af608d1a",
      "metadata": {
        "id": "af608d1a"
      },
      "source": [
        "# Lead Time"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "id": "b3d5e69d",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b3d5e69d",
        "outputId": "3502c9d4-47e6-4283-ab65-ebab2a608a8b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   lead_time  lead_time_normalized\n",
            "0        342              5.837730\n",
            "1        737              6.603944\n",
            "2          7              2.079442\n",
            "3         13              2.639057\n",
            "4         14              2.708050\n"
          ]
        }
      ],
      "source": [
        "# Apply logarithmic transformation to \"lead_time\"\n",
        "df['lead_time_normalized'] = np.log1p(df['lead_time'])\n",
        "\n",
        "# Display the first few rows of the DataFrame with the normalized column\n",
        "print(df[['lead_time', 'lead_time_normalized']].head())\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "id": "0f77ba2e",
      "metadata": {
        "id": "0f77ba2e"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"lead_time\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "6a9fcb20",
      "metadata": {
        "id": "6a9fcb20"
      },
      "source": [
        "# Arrival Date (Year, Month, Day of Month)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "id": "be5c659f",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "be5c659f",
        "outputId": "6c87c050-ebeb-4e9e-e1c6-e63c236c3375"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['July', 'August', 'September', 'October', 'November', 'December',\n",
              "       'January', 'February', 'March', 'April', 'May', 'June'],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ],
      "source": [
        "class_names=df[\"arrival_date_month\"].unique()\n",
        "class_names"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "id": "7c6187be",
      "metadata": {
        "id": "7c6187be"
      },
      "outputs": [],
      "source": [
        "df.loc[ df[\"arrival_date_month\"] == class_names[0],\"arrival_date_month\"]=7\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[1],\"arrival_date_month\"]=8\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[2],\"arrival_date_month\"]=9\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[3],\"arrival_date_month\"]=10\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[4],\"arrival_date_month\"]=11\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[5],\"arrival_date_month\"]=12\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[6],\"arrival_date_month\"]=1\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[7],\"arrival_date_month\"]=2\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[8],\"arrival_date_month\"]=3\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[9],\"arrival_date_month\"]=4\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[10],\"arrival_date_month\"]=5\n",
        "df.loc[ df[\"arrival_date_month\"] == class_names[11],\"arrival_date_month\"]=6\n",
        "df[\"arrival_date_month\"] = df[\"arrival_date_month\"].astype(int)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "id": "20c1f2cd",
      "metadata": {
        "id": "20c1f2cd"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"arrival_date_day_of_month\"],axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "id": "6dba446c",
      "metadata": {
        "id": "6dba446c"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"arrival_date_week_number\"],axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V7_2C3E3vQen",
        "outputId": "b7f5506f-fa1c-4619-dbf6-c74816d5f2bd"
      },
      "id": "V7_2C3E3vQen",
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['hotel', 'is_canceled', 'arrival_date_year', 'arrival_date_month',\n",
              "       'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children',\n",
              "       'babies', 'meal', 'country', 'market_segment', 'distribution_channel',\n",
              "       'is_repeated_guest', 'previous_cancellations',\n",
              "       'previous_bookings_not_canceled', 'reserved_room_type',\n",
              "       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',\n",
              "       'days_in_waiting_list', 'customer_type', 'adr',\n",
              "       'required_car_parking_spaces', 'total_of_special_requests',\n",
              "       'reservation_status', 'reservation_status_date',\n",
              "       'lead_time_normalized'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b6eea128",
      "metadata": {
        "id": "b6eea128"
      },
      "source": [
        "# Weekdays & Week nights"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "id": "76a50499",
      "metadata": {
        "id": "76a50499"
      },
      "outputs": [],
      "source": [
        "df[\"total_stays\"]=df[\"stays_in_weekend_nights\"]+df[\"stays_in_week_nights\"]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "id": "52340e31",
      "metadata": {
        "id": "52340e31"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"stays_in_week_nights\"],axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "id": "e2cf85de",
      "metadata": {
        "id": "e2cf85de"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"stays_in_weekend_nights\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "bf9beb25",
      "metadata": {
        "id": "bf9beb25"
      },
      "source": [
        "# Adults"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "id": "4cc63dae",
      "metadata": {
        "id": "4cc63dae"
      },
      "outputs": [],
      "source": [
        "df.drop(df[df[\"adults\"]==0].index,inplace=True)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "af7a0775",
      "metadata": {
        "id": "af7a0775"
      },
      "source": [
        "# Children & Babies"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "id": "97c58101",
      "metadata": {
        "id": "97c58101"
      },
      "outputs": [],
      "source": [
        "df['kids'] = df['children'] + df['babies']\n",
        "df[\"kids\"] = df[\"kids\"].astype(int)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "df79ab95",
      "metadata": {
        "id": "df79ab95"
      },
      "source": [
        "# Meal Type"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "id": "153aaf97",
      "metadata": {
        "id": "153aaf97"
      },
      "outputs": [],
      "source": [
        "df=df.replace(\"Undefined\",\"SC\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "id": "27e7126d",
      "metadata": {
        "id": "27e7126d"
      },
      "outputs": [],
      "source": [
        "\n",
        "df[\"BB\"] = df['meal'].apply(lambda x: 1 if x == 'BB' else 0)\n",
        "\n",
        "df[\"FB\"] = df['meal'].apply(lambda x: 1 if x == 'FB' else 0)\n",
        "\n",
        "df[\"HB\"] = df['meal'].apply(lambda x: 1 if x == 'HB' else 0)\n",
        "\n",
        "df[\"SC\"] = df['meal'].apply(lambda x: 1 if x == 'SC' else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "id": "115d4b66",
      "metadata": {
        "id": "115d4b66"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"meal\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "549640a5",
      "metadata": {
        "id": "549640a5"
      },
      "source": [
        "# Country"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "id": "24eda97e",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "24eda97e",
        "outputId": "60e72a8f-b355-4347-80f5-e5bc5b710337"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[135  59 169  51  76  56 139 124 127   6 133  43  15  29  34  66  81 123\n",
            "  46 140 154  11  52  42  25  54 113  27 100 153   3  75  31 107 103 166\n",
            " 148 101 134 149  30  12  23  99 162 174   1  80  40 175  37 176  48  91\n",
            "  38  72   5 161  82  71  69  77  60   4  63 168  83  28  41  35  61  92\n",
            " 121 106 171 152  55  86 128  73  94 131 144 155  13  20 126 158  47 108\n",
            " 117   7  85  98  39  33  22 115  36 151 165  19  32  84 156 145  14 142\n",
            " 173 132 138  50 130 110 116  49 105  79 170 125  21 102 157 163  44 150\n",
            "  90  53  78  70 141  88 104  18  74 159 122  16 172 164  58  62 160  64\n",
            "  87  97  65 112 167 118  57 111 129  17  95 109 119  24 136  26   0   2\n",
            " 147  45 137  68  96   9  67   8 114 120  89 143  10 146  93]\n"
          ]
        }
      ],
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "\n",
        "# Initialize LabelEncoder\n",
        "label_encoder = LabelEncoder()\n",
        "\n",
        "# Encode the country column\n",
        "df['country'] = label_encoder.fit_transform(df['country'])\n",
        "\n",
        "# Display the unique encoded values\n",
        "encoded_values = df['country'].unique()\n",
        "print(encoded_values)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "cbe2f7e7",
      "metadata": {
        "id": "cbe2f7e7"
      },
      "source": [
        "# Market Segment"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "id": "ae6a6978",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ae6a6978",
        "outputId": "89caa8aa-77d4-44e3-ee7c-cf9a67c08cb2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Direct', 'Corporate', 'Online TA', 'Offline TA/TO',\n",
              "       'Complementary', 'Groups', 'Aviation'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ],
      "source": [
        "unique_values = df['market_segment'].unique()\n",
        "unique_values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "id": "d78ba532",
      "metadata": {
        "id": "d78ba532"
      },
      "outputs": [],
      "source": [
        "\n",
        "df[\"Direct\"] = df['market_segment'].apply(lambda x: 1 if x == 'Direct' else 0)\n",
        "\n",
        "df[\"Corporate\"] = df['market_segment'].apply(lambda x: 1 if x == 'Corporate' else 0)\n",
        "\n",
        "df[\"Online TA\"] = df['market_segment'].apply(lambda x: 1 if x == 'Online TA' else 0)\n",
        "\n",
        "df[\"Offline TA/TO\"] = df['market_segment'].apply(lambda x: 1 if x == 'Offline TA/TO' else 0)\n",
        "\n",
        "df[\"Complementary\"] = df['market_segment'].apply(lambda x: 1 if x == 'Complementary' else 0)\n",
        "\n",
        "df[\"Groups\"] = df['market_segment'].apply(lambda x: 1 if x == 'Groups' else 0)\n",
        "\n",
        "df[\"Aviation\"] = df['market_segment'].apply(lambda x: 1 if x == 'Aviation' else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "id": "1529224b",
      "metadata": {
        "id": "1529224b"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"market_segment\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fb516222",
      "metadata": {
        "id": "fb516222"
      },
      "source": [
        "# Distribution Channel"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "id": "f3eddc8a",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3eddc8a",
        "outputId": "0230068b-0fb1-443d-e87d-0ef03784626f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Direct', 'Corporate', 'TA/TO', 'SC', 'GDS'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ],
      "source": [
        "unique_values = df['distribution_channel'].unique()\n",
        "unique_values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "id": "ed410c99",
      "metadata": {
        "id": "ed410c99"
      },
      "outputs": [],
      "source": [
        "df[\"Dist Direct\"] = df['distribution_channel'].apply(lambda x: 1 if x == 'Direct' else 0)\n",
        "\n",
        "df[\"Dist Corporate\"] = df['distribution_channel'].apply(lambda x: 1 if x == 'Corporate' else 0)\n",
        "\n",
        "df[\"Dist TA/TO\"] = df['distribution_channel'].apply(lambda x: 1 if x == 'TA/TO' else 0)\n",
        "\n",
        "df[\"SC\"] = df['distribution_channel'].apply(lambda x: 1 if x == 'SC' else 0)\n",
        "\n",
        "df[\"GDS\"] = df['distribution_channel'].apply(lambda x: 1 if x == 'GDS' else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "id": "f4f176d1",
      "metadata": {
        "id": "f4f176d1"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"distribution_channel\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "d250ffae",
      "metadata": {
        "id": "d250ffae"
      },
      "source": [
        "# Reserved & Assigned Room Type"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "id": "bf6aac5f",
      "metadata": {
        "id": "bf6aac5f"
      },
      "outputs": [],
      "source": [
        "class_names = df['assigned_room_type'].unique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "id": "ba42c13a",
      "metadata": {
        "id": "ba42c13a"
      },
      "outputs": [],
      "source": [
        "for i in range(len(class_names)):\n",
        "    df.loc[ df['assigned_room_type'] == class_names[i],'assigned_room_type']=i"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 41,
      "id": "3bdfa2b1",
      "metadata": {
        "id": "3bdfa2b1"
      },
      "outputs": [],
      "source": [
        "class_names2 = df['reserved_room_type'].unique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 42,
      "id": "656dfe04",
      "metadata": {
        "id": "656dfe04"
      },
      "outputs": [],
      "source": [
        "for i in range(len(class_names2)):\n",
        "    df.loc[ df['reserved_room_type'] == class_names2[i],'reserved_room_type']=i"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "92b36591",
      "metadata": {
        "id": "92b36591"
      },
      "source": [
        "# Deposit Type"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 43,
      "id": "4c41b15b",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4c41b15b",
        "outputId": "42612fc0-2ad1-421e-8149-93ec35648958"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['No Deposit', 'Refundable', 'Non Refund'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ],
      "source": [
        "unique_values = df['deposit_type'].unique()\n",
        "unique_values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 44,
      "id": "da52697c",
      "metadata": {
        "id": "da52697c"
      },
      "outputs": [],
      "source": [
        "df[\"No Deposit\"] = df['deposit_type'].apply(lambda x: 1 if x == 'No Deposit' else 0)\n",
        "\n",
        "df[\"Refundable\"] = df['deposit_type'].apply(lambda x: 1 if x == 'Refundable' else 0)\n",
        "\n",
        "df[\"Non Refund\"] = df['deposit_type'].apply(lambda x: 1 if x == 'Non Refund' else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 45,
      "id": "ddd32324",
      "metadata": {
        "id": "ddd32324"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"deposit_type\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "13cf5bda",
      "metadata": {
        "id": "13cf5bda"
      },
      "source": [
        "# Customer Type"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 46,
      "id": "e3f2acf6",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e3f2acf6",
        "outputId": "877e0eee-0c8c-43b0-c392-2fca32e18a61"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Transient', 'Contract', 'Transient-Party', 'Group'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ],
      "source": [
        "unique_values = df['customer_type'].unique()\n",
        "unique_values"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 47,
      "id": "056a686f",
      "metadata": {
        "id": "056a686f"
      },
      "outputs": [],
      "source": [
        "df[\"Transient\"] = df['customer_type'].apply(lambda x: 1 if x == 'Transient' else 0)\n",
        "\n",
        "df[\"Contract\"] = df['customer_type'].apply(lambda x: 1 if x == 'Contract' else 0)\n",
        "\n",
        "df[\"Transient-Party\"] = df['customer_type'].apply(lambda x: 1 if x == 'Transient-Party' else 0)\n",
        "\n",
        "df[\"Group\"] = df['customer_type'].apply(lambda x: 1 if x == 'Group' else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 48,
      "id": "de21519c",
      "metadata": {
        "id": "de21519c"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"customer_type\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f1e4a430",
      "metadata": {
        "id": "f1e4a430"
      },
      "source": [
        "# ADR"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 49,
      "id": "a6737f58",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 227
        },
        "id": "a6737f58",
        "outputId": "95495cc8-cb2d-45d0-a27b-9556fc1b80ff"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       hotel  is_canceled  arrival_date_year  arrival_date_month  adults  \\\n",
              "15083      0            0               2015                   7       2   \n",
              "48515      1            1               2016                   3       2   \n",
              "111403     1            0               2017                   5       1   \n",
              "\n",
              "        children  babies  country  is_repeated_guest  previous_cancellations  \\\n",
              "15083        0.0       0      135                  1                       0   \n",
              "48515        0.0       0      135                  0                       0   \n",
              "111403       0.0       0       81                  0                       0   \n",
              "\n",
              "        ...  Dist Corporate Dist TA/TO GDS  No Deposit  Refundable  \\\n",
              "15083   ...               1          0   0           1           0   \n",
              "48515   ...               0          1   0           0           0   \n",
              "111403  ...               0          1   0           1           0   \n",
              "\n",
              "        Non Refund  Transient  Contract  Transient-Party Group  \n",
              "15083            0          1         0                0     0  \n",
              "48515            1          1         0                0     0  \n",
              "111403           0          1         0                0     0  \n",
              "\n",
              "[3 rows x 46 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ffbcd69a-ea90-48fc-ac5b-64b72a0a9699\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>hotel</th>\n",
              "      <th>is_canceled</th>\n",
              "      <th>arrival_date_year</th>\n",
              "      <th>arrival_date_month</th>\n",
              "      <th>adults</th>\n",
              "      <th>children</th>\n",
              "      <th>babies</th>\n",
              "      <th>country</th>\n",
              "      <th>is_repeated_guest</th>\n",
              "      <th>previous_cancellations</th>\n",
              "      <th>...</th>\n",
              "      <th>Dist Corporate</th>\n",
              "      <th>Dist TA/TO</th>\n",
              "      <th>GDS</th>\n",
              "      <th>No Deposit</th>\n",
              "      <th>Refundable</th>\n",
              "      <th>Non Refund</th>\n",
              "      <th>Transient</th>\n",
              "      <th>Contract</th>\n",
              "      <th>Transient-Party</th>\n",
              "      <th>Group</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>15083</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>135</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>48515</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2016</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>135</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>111403</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2017</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>81</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>3 rows × 46 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ffbcd69a-ea90-48fc-ac5b-64b72a0a9699')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ffbcd69a-ea90-48fc-ac5b-64b72a0a9699 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ffbcd69a-ea90-48fc-ac5b-64b72a0a9699');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-b7112c79-8b8f-44b4-922a-caa13a45aa7c\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-b7112c79-8b8f-44b4-922a-caa13a45aa7c')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-b7112c79-8b8f-44b4-922a-caa13a45aa7c button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe"
            }
          },
          "metadata": {},
          "execution_count": 49
        }
      ],
      "source": [
        "df[df[\"adr\"]>500]"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "857a96fb",
      "metadata": {
        "id": "857a96fb"
      },
      "source": [
        "# Reservation Status"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 50,
      "id": "64ac4768",
      "metadata": {
        "id": "64ac4768"
      },
      "outputs": [],
      "source": [
        "df=df.drop([\"reservation_status\"],axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "fde77632",
      "metadata": {
        "id": "fde77632"
      },
      "source": [
        "# Reservation Date"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 51,
      "id": "ff7a7f59",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ff7a7f59",
        "outputId": "2bef7bad-a859-4751-83f5-bd243c1400a7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  hotel  is_canceled  arrival_date_year  arrival_date_month  adults  children  \\\n",
            "0     0            0               2015                   7       2       0.0   \n",
            "1     0            0               2015                   7       2       0.0   \n",
            "2     0            0               2015                   7       1       0.0   \n",
            "3     0            0               2015                   7       1       0.0   \n",
            "4     0            0               2015                   7       2       0.0   \n",
            "\n",
            "   babies  country  is_repeated_guest  previous_cancellations  ...  GDS  \\\n",
            "0       0      135                  0                       0  ...    0   \n",
            "1       0      135                  0                       0  ...    0   \n",
            "2       0       59                  0                       0  ...    0   \n",
            "3       0       59                  0                       0  ...    0   \n",
            "4       0       59                  0                       0  ...    0   \n",
            "\n",
            "  No Deposit Refundable  Non Refund  Transient  Contract  Transient-Party  \\\n",
            "0          1          0           0          1         0                0   \n",
            "1          1          0           0          1         0                0   \n",
            "2          1          0           0          1         0                0   \n",
            "3          1          0           0          1         0                0   \n",
            "4          1          0           0          1         0                0   \n",
            "\n",
            "   Group  reservation_year  reservation_month  \n",
            "0      0              2015                  7  \n",
            "1      0              2015                  7  \n",
            "2      0              2015                  7  \n",
            "3      0              2015                  7  \n",
            "4      0              2015                  7  \n",
            "\n",
            "[5 rows x 46 columns]\n"
          ]
        }
      ],
      "source": [
        "# Convert 'reservation_status_date' to datetime type with custom format\n",
        "df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format='%d/%m/%Y')\n",
        "\n",
        "# Extract year and month from 'reservation_status_date'\n",
        "df['reservation_year'] = df['reservation_status_date'].dt.year\n",
        "df['reservation_month'] = df['reservation_status_date'].dt.month\n",
        "\n",
        "# Drop the original 'reservation_status_date' column\n",
        "df.drop(columns=['reservation_status_date'], inplace=True)\n",
        "\n",
        "# Display the first few rows of the DataFrame with the new columns\n",
        "print(df.head())\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "46319935",
      "metadata": {
        "id": "46319935"
      },
      "source": [
        "# New Feature \"Total Guests\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 52,
      "id": "f9e0af39",
      "metadata": {
        "id": "f9e0af39"
      },
      "outputs": [],
      "source": [
        "df[\"total_guests\"]=df[\"adults\"]+df[\"kids\"]"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "9baa0328",
      "metadata": {
        "id": "9baa0328"
      },
      "source": [
        "# Post Data Cleaning"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 53,
      "id": "bde2dd8f",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bde2dd8f",
        "outputId": "2a8e1bdf-a106-472e-8791-1320f8e0c7d9"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['hotel', 'is_canceled', 'arrival_date_year', 'arrival_date_month',\n",
              "       'adults', 'children', 'babies', 'country', 'is_repeated_guest',\n",
              "       'previous_cancellations', 'previous_bookings_not_canceled',\n",
              "       'reserved_room_type', 'assigned_room_type', 'booking_changes', 'agent',\n",
              "       'days_in_waiting_list', 'adr', 'required_car_parking_spaces',\n",
              "       'total_of_special_requests', 'lead_time_normalized', 'total_stays',\n",
              "       'kids', 'BB', 'FB', 'HB', 'SC', 'Direct', 'Corporate', 'Online TA',\n",
              "       'Offline TA/TO', 'Complementary', 'Groups', 'Aviation', 'Dist Direct',\n",
              "       'Dist Corporate', 'Dist TA/TO', 'GDS', 'No Deposit', 'Refundable',\n",
              "       'Non Refund', 'Transient', 'Contract', 'Transient-Party', 'Group',\n",
              "       'reservation_year', 'reservation_month', 'total_guests'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ],
      "source": [
        "df.columns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from scipy import stats\n",
        "\n",
        "# Step 1: Identify numerical columns\n",
        "numerical_columns = df.select_dtypes(include=np.number).columns\n",
        "\n",
        "# Step 2: Calculate z-scores for each numerical column\n",
        "z_scores = np.abs(stats.zscore(df[numerical_columns]))\n",
        "\n",
        "# Step 3: Define threshold for z-score\n",
        "threshold = 3  # You can adjust this threshold as needed\n",
        "\n",
        "# Step 4: Drop rows with outliers in any numerical column\n",
        "df_no_outliers = df[(z_scores < threshold).all(axis=1)]\n",
        "\n",
        "# Display the shape of the original and cleaned DataFrames\n",
        "print(\"Original DataFrame shape:\", df.shape)\n",
        "print(\"DataFrame shape after dropping outliers:\", df_no_outliers.shape)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LHPrK30zw6gu",
        "outputId": "a0b8229a-ef1f-4947-ded9-184845933d85"
      },
      "id": "LHPrK30zw6gu",
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original DataFrame shape: (118983, 47)\n",
            "DataFrame shape after dropping outliers: (87041, 47)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 55,
      "id": "3ed6b6c3",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ed6b6c3",
        "outputId": "2fc91fda-3ee5-40b5-bc32-452988cf1a20"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "47"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ],
      "source": [
        "num_columns = df.shape[1]\n",
        "num_columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 56,
      "id": "8ba26cfb",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8ba26cfb",
        "outputId": "fdcac4ae-b968-4ec7-c996-c7c13cc25a68"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "118983"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ],
      "source": [
        "num_observations = len(df)\n",
        "num_observations"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 57,
      "id": "95662379",
      "metadata": {
        "id": "95662379"
      },
      "outputs": [],
      "source": [
        "\n",
        "df_no_outliers.to_csv('Post-cleaning Data.csv', index=False, mode='w')\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 58,
      "id": "aa82d76d",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 273
        },
        "id": "aa82d76d",
        "outputId": "299b7a20-ef7d-450a-d12d-5d17f6d2468b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  hotel  is_canceled  arrival_date_year  arrival_date_month  adults  children  \\\n",
              "2     0            0               2015                   7       1       0.0   \n",
              "4     0            0               2015                   7       2       0.0   \n",
              "5     0            0               2015                   7       2       0.0   \n",
              "6     0            0               2015                   7       2       0.0   \n",
              "8     0            1               2015                   7       2       0.0   \n",
              "\n",
              "   babies  country  is_repeated_guest  previous_cancellations  ...  \\\n",
              "2       0       59                  0                       0  ...   \n",
              "4       0       59                  0                       0  ...   \n",
              "5       0       59                  0                       0  ...   \n",
              "6       0      135                  0                       0  ...   \n",
              "8       0      135                  0                       0  ...   \n",
              "\n",
              "   No Deposit Refundable Non Refund  Transient  Contract  Transient-Party  \\\n",
              "2           1          0          0          1         0                0   \n",
              "4           1          0          0          1         0                0   \n",
              "5           1          0          0          1         0                0   \n",
              "6           1          0          0          1         0                0   \n",
              "8           1          0          0          1         0                0   \n",
              "\n",
              "   Group  reservation_year  reservation_month  total_guests  \n",
              "2      0              2015                  7             1  \n",
              "4      0              2015                  7             2  \n",
              "5      0              2015                  7             2  \n",
              "6      0              2015                  7             2  \n",
              "8      0              2015                  5             2  \n",
              "\n",
              "[5 rows x 47 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-78f76123-6367-4499-a91d-5eaba9912fcf\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>hotel</th>\n",
              "      <th>is_canceled</th>\n",
              "      <th>arrival_date_year</th>\n",
              "      <th>arrival_date_month</th>\n",
              "      <th>adults</th>\n",
              "      <th>children</th>\n",
              "      <th>babies</th>\n",
              "      <th>country</th>\n",
              "      <th>is_repeated_guest</th>\n",
              "      <th>previous_cancellations</th>\n",
              "      <th>...</th>\n",
              "      <th>No Deposit</th>\n",
              "      <th>Refundable</th>\n",
              "      <th>Non Refund</th>\n",
              "      <th>Transient</th>\n",
              "      <th>Contract</th>\n",
              "      <th>Transient-Party</th>\n",
              "      <th>Group</th>\n",
              "      <th>reservation_year</th>\n",
              "      <th>reservation_month</th>\n",
              "      <th>total_guests</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>59</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>59</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>59</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>135</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2015</td>\n",
              "      <td>7</td>\n",
              "      <td>2</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>135</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2015</td>\n",
              "      <td>5</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 47 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-78f76123-6367-4499-a91d-5eaba9912fcf')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-78f76123-6367-4499-a91d-5eaba9912fcf button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-78f76123-6367-4499-a91d-5eaba9912fcf');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-e6eb313f-3378-421d-b437-03544e67c821\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e6eb313f-3378-421d-b437-03544e67c821')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-e6eb313f-3378-421d-b437-03544e67c821 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df_no_outliers"
            }
          },
          "metadata": {},
          "execution_count": 58
        }
      ],
      "source": [
        "df_no_outliers.head()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Path to the CSV file in your Google Drive\n",
        "file_path = 'Post-cleaning Data.csv'\n",
        "\n",
        "# Read the CSV file into a DataFrame\n",
        "df = pd.read_csv(file_path)"
      ],
      "metadata": {
        "id": "PFhD6kiPxXIM"
      },
      "id": "PFhD6kiPxXIM",
      "execution_count": 59,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.metrics import roc_curve, roc_auc_score, recall_score, precision_score, confusion_matrix\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.metrics import recall_score\n",
        "from sklearn.metrics import accuracy_score\n",
        "from sklearn.metrics import precision_score\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.neural_network import MLPClassifier\n",
        "from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier\n",
        "from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler\n",
        "from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV\n",
        "from sklearn.feature_selection import SelectFromModel, SelectPercentile\n",
        "from sklearn.metrics import f1_score, confusion_matrix\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "from sklearn.metrics import roc_curve, roc_auc_score, recall_score, precision_score, confusion_matrix"
      ],
      "metadata": {
        "id": "F7sAKtmzxmAm"
      },
      "id": "F7sAKtmzxmAm",
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train = df.drop(['is_canceled'], axis=1)\n",
        "test = df['is_canceled']\n",
        "train = train.iloc[:,1:]"
      ],
      "metadata": {
        "id": "iQhIup6KxdXa"
      },
      "id": "iQhIup6KxdXa",
      "execution_count": 61,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.20)\n",
        "X_train.shape, y_train.shape, X_test.shape, y_test.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DR_z_OBQxhT8",
        "outputId": "ba0410cc-7666-4d75-8712-8d46bc297354"
      },
      "id": "DR_z_OBQxhT8",
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "((69632, 45), (69632,), (17409, 45), (17409,))"
            ]
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.random.seed(2002)"
      ],
      "metadata": {
        "id": "W2fIPEw4xnzi"
      },
      "id": "W2fIPEw4xnzi",
      "execution_count": 63,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rd_clf = RandomForestClassifier()\n",
        "rd_clf.fit(X_train, y_train)\n",
        "\n",
        "y_pred_rd_clf = rd_clf.predict(X_test)\n",
        "\n",
        "acc_rd_clf = accuracy_score(y_test, y_pred_rd_clf)\n",
        "conf = confusion_matrix(y_test, y_pred_rd_clf)\n",
        "clf_report = classification_report(y_test, y_pred_rd_clf)\n",
        "\n",
        "print(f\"Accuracy Score of Random Forest is : {acc_rd_clf}\")\n",
        "print(\"F1 score: {:.3f}\".format(f1_score(y_test, y_pred_rd_clf)))\n",
        "print(f\"Classification Report : \\n{clf_report}\")\n",
        "confusion = confusion_matrix(y_test, y_pred_rd_clf)\n",
        "df_cm = pd.DataFrame(confusion)\n",
        "sns.heatmap(df_cm, annot=True,fmt=\"g\",cmap=\"YlGnBu\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 656
        },
        "id": "VBKKhOstxrth",
        "outputId": "b2978506-caff-49a5-f9f0-68801160aac5"
      },
      "id": "VBKKhOstxrth",
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy Score of Random Forest is : 0.9294739260280267\n",
            "F1 score: 0.910\n",
            "Classification Report : \n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.97      0.94      2574\n",
            "           1       0.95      0.88      0.91      1779\n",
            "\n",
            "    accuracy                           0.93      4353\n",
            "   macro avg       0.93      0.92      0.93      4353\n",
            "weighted avg       0.93      0.93      0.93      4353\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 86
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import log_loss\n",
        "\n",
        "# Predict probabilities for evaluation\n",
        "y_pred_proba = rd_clf.predict_proba(X_test)\n",
        "\n",
        "# Calculate binary cross-entropy loss\n",
        "binary_crossentropy_loss = log_loss(y_test, y_pred_proba)\n",
        "print(\"Binary Cross-Entropy Loss:\", binary_crossentropy_loss)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cTCICR6-ydBI",
        "outputId": "e3507cd5-02f2-40f8-cfb9-d8bc4bec80ce"
      },
      "id": "cTCICR6-ydBI",
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Binary Cross-Entropy Loss: 0.20634102486613903\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "\n",
        "\n",
        "# Assuming df_new is your DataFrame containing the dataset\n",
        "\n",
        "# Create a data partition for the variable \"is_canceled\"\n",
        "X = df.drop(columns=['is_canceled'])  # Features\n",
        "y = df['is_canceled']  # Target variable\n",
        "\n",
        "# Create the training and test sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)\n",
        "\n",
        "# Initialize the Random Forest classifier\n",
        "rf_clf = RandomForestClassifier()\n",
        "\n",
        "# Train the model on the training data\n",
        "rf_clf.fit(X_train, y_train)\n",
        "\n",
        "# Predict the target variable on the test data\n",
        "y_pred = rf_clf.predict(X_test)\n",
        "\n",
        "# Calculate the accuracy of the model\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(\"Accuracy:\", accuracy)\n",
        "print(\"F1 score: {:.3f}\".format(f1_score(y_test, y_pred)))\n",
        "print(f\"Classification Report : \\n{clf_report}\")\n",
        "confusion = confusion_matrix(y_test, y_pred)\n",
        "df_cm = pd.DataFrame(confusion)\n",
        "sns.heatmap(df_cm, annot=True,fmt=\"g\",cmap=\"YlGnBu\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 656
        },
        "id": "Pc9G_YHTziLB",
        "outputId": "a90e4611-7a55-4a62-8ea9-23c8fadc8d31"
      },
      "id": "Pc9G_YHTziLB",
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.9260280266482885\n",
            "F1 score: 0.907\n",
            "Classification Report : \n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.97      0.94      2574\n",
            "           1       0.95      0.88      0.91      1779\n",
            "\n",
            "    accuracy                           0.93      4353\n",
            "   macro avg       0.93      0.92      0.93      4353\n",
            "weighted avg       0.93      0.93      0.93      4353\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 89
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import log_loss\n",
        "\n",
        "# Predict probabilities for evaluation\n",
        "y_pred_proba = rd_clf.predict_proba(X_test)\n",
        "\n",
        "# Calculate binary cross-entropy loss\n",
        "binary_crossentropy_loss = log_loss(y_test, y_pred_proba)\n",
        "print(\"Binary Cross-Entropy Loss:\", binary_crossentropy_loss)"
      ],
      "metadata": {
        "id": "XxjGibsg4t_7"
      },
      "id": "XxjGibsg4t_7",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "\n",
        "\n",
        "# Assuming df_new is your DataFrame containing the dataset\n",
        "\n",
        "# Create a data partition for the variable \"is_canceled\"\n",
        "X = df.drop(columns=['is_canceled'])  # Features\n",
        "y = df['is_canceled']  # Target variable\n",
        "\n",
        "# Create the training and test sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)\n",
        "\n",
        "# Initialize the Random Forest classifier\n",
        "rf_clf = RandomForestClassifier(n_estimators=1000,\n",
        "    min_samples_split=3,\n",
        "    min_samples_leaf=2,\n",
        "    max_features='log2',\n",
        "    max_depth=100,\n",
        "    bootstrap=False)\n",
        "\n",
        "# Train the model on the training data\n",
        "rf_clf.fit(X_train, y_train)\n",
        "\n",
        "# Predict the target variable on the test data\n",
        "y_pred = rf_clf.predict(X_test)\n",
        "\n",
        "# Calculate the accuracy of the model\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(\"Accuracy:\", accuracy)\n",
        "print(\"F1 score: {:.3f}\".format(f1_score(y_test, y_pred)))\n",
        "print(f\"Classification Report : \\n{clf_report}\")\n",
        "confusion = confusion_matrix(y_test, y_pred)\n",
        "df_cm = pd.DataFrame(confusion)\n",
        "sns.heatmap(df_cm, annot=True,fmt=\"g\",cmap=\"YlGnBu\")\n"
      ],
      "metadata": {
        "id": "gY7MYkqd3McJ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 656
        },
        "outputId": "7b26f6d4-4793-4ace-ca87-714f436a28a0"
      },
      "id": "gY7MYkqd3McJ",
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.9292441994027107\n",
            "F1 score: 0.910\n",
            "Classification Report : \n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.97      0.94      2574\n",
            "           1       0.95      0.88      0.91      1779\n",
            "\n",
            "    accuracy                           0.93      4353\n",
            "   macro avg       0.93      0.92      0.93      4353\n",
            "weighted avg       0.93      0.93      0.93      4353\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 91
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix\n",
        "import seaborn as sns\n",
        "\n",
        "# Assuming df_new is your DataFrame containing the dataset\n",
        "\n",
        "# Create a data partition for the variable \"is_canceled\"\n",
        "X = df.drop(columns=['is_canceled'])  # Features\n",
        "y = df['is_canceled']  # Target variable\n",
        "\n",
        "# Create the training and test sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)\n",
        "\n",
        "# Initialize the Random Forest classifier\n",
        "rf_clf = RandomForestClassifier()\n",
        "\n",
        "# Train the model on the training data\n",
        "rf_clf.fit(X_train, y_train)\n",
        "\n",
        "# Predict the target variable on the training data\n",
        "y_train_pred = rf_clf.predict(X_train)\n",
        "\n",
        "# Calculate the accuracy of the model on the training data\n",
        "train_accuracy = accuracy_score(y_train, y_train_pred)\n",
        "print(\"Training Accuracy:\", train_accuracy)\n",
        "\n",
        "# Predict the target variable on the test data\n",
        "y_test_pred = rf_clf.predict(X_test)\n",
        "\n",
        "# Calculate the accuracy of the model on the test data\n",
        "test_accuracy = accuracy_score(y_test, y_test_pred)\n",
        "print(\"Test Accuracy:\", test_accuracy)\n",
        "\n",
        "# Additional evaluation metrics\n",
        "print(\"F1 score: {:.3f}\".format(f1_score(y_test, y_test_pred)))\n",
        "print(\"Classification Report:\")\n",
        "print(classification_report(y_test, y_test_pred))\n",
        "print(\"Confusion Matrix:\")\n",
        "confusion = confusion_matrix(y_test, y_test_pred)\n",
        "df_cm = pd.DataFrame(confusion)\n",
        "sns.heatmap(df_cm, annot=True, fmt=\"g\", cmap=\"YlGnBu\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 691
        },
        "id": "4rTDs8vCxxXP",
        "outputId": "2499a45f-3462-459d-da2e-aaec8e197cd1"
      },
      "id": "4rTDs8vCxxXP",
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training Accuracy: 0.996517027863777\n",
            "Test Accuracy: 0.9377440845393982\n",
            "F1 score: 0.921\n",
            "Classification Report:\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.93      0.97      0.95      2568\n",
            "           1       0.96      0.89      0.92      1785\n",
            "\n",
            "    accuracy                           0.94      4353\n",
            "   macro avg       0.94      0.93      0.93      4353\n",
            "weighted avg       0.94      0.94      0.94      4353\n",
            "\n",
            "Confusion Matrix:\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 92
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhAAAAGdCAYAAABDxkoSAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAoJ0lEQVR4nO3deXhU5d3/8c9kGxZJwpZMooCxKpsINGCIAopEArJWXEAqqFGqTaiQihbrA4jWWETZ1Ye6gC3yoFapgiIBRFoIBKJBQEFRILhMWGISE8gkJPP7wx+jcwc4HJ04Kb5f13WuqznnnpN7Tkvzme/3PmccXq/XKwAAABtCgj0BAADw34cAAQAAbCNAAAAA2wgQAADANgIEAACwjQABAABsI0AAAADbCBAAAMA2AgQAALAtLNgTOKFh65HBngJQ7xwreCjYUwDqqYvr9OyB/Jt0rGBJwM5Vn9SbAAEAQH3hcFCgt8IVAgAAtlGBAADA4ODztSUCBAAABloY1ggQAAAYCBDWuEIAAMA2KhAAABgcDkewp1DvESAAAKiFAr0VrhAAALCNCgQAAAYWUVojQAAAYCBAWOMKAQAA26hAAABg4EmU1ggQAAAYaGFY4woBAADbqEAAAGCgAmGNAAEAgIEAYY0AAQCAwSEeZW2FiAUAAGyjAgEAgIEWhjUCBAAABgKENa4QAACwjQoEAAAGKhDWCBAAANRCgLDCFQIAALZRgQAAwEALwxoBAgAAAwHCGlcIAADYRgUCAACDg8/XlggQAAAYaGFYI0AAAGBwOPgyLStELAAAYBsVCAAADLQwrBEgAAAwsIjSGlcIAADYRgUCAAADLQxrBAgAAAwECGtcIQAAYBsVCAAADCyitEaAAADARAvDElcIAADYRgUCAAADiyitESAAADDwXRjWCBAAABhYRGmNKwQAAGyjAgEAgIE1ENYIEAAAmFgDYYmIBQAAbKMCAQCAiY/XlggQAACYaGFYImMBAADbqEAAAGCiAmGJAAEAgIn6vCUuEQAAsI0KBAAABi8tDEsECAAATOQHSwQIAABMISQIK6yBAAAAtlGBAADAxBoISwQIAABM5AdLtDAAAIBtVCAAADCxiNISAQIAABNrICzRwgAAALZRgQAAwEQBwhIBAgAAE2sgLNHCAAAAtlGBAADARAHCEgECAAAD38ZpjQABAICJNRCWWAMBAEA9kZWVpe7du6tJkyaKiYnRsGHDtHv3br8xFRUVSk9PV/PmzXXOOedo+PDhKiws9BtTUFCggQMHqlGjRoqJidHEiRN1/PhxvzHr1q3Tr3/9azmdTl144YVauHChrbkSIAAAMDkCuNnw3nvvKT09XZs2bVJ2draqqqrUr18/lZeX+8ZMmDBBb775pl555RW99957+uqrr3Tdddf5jldXV2vgwIGqrKzUxo0btWjRIi1cuFCTJ0/2jdm7d68GDhyoPn36KD8/X+PHj9cdd9yhd95558wvkdfr9dp7e3WjYeuRwZ4CUO8cK3go2FMA6qmL6/TsFw5ZFLBz7XljzI9+7aFDhxQTE6P33ntPvXv3VklJiVq2bKmXXnpJ119/vSRp165dat++vXJyctSjRw+9/fbbGjRokL766ivFxsZKkp555hndf//9OnTokCIiInT//fdrxYoV2rFjh+93jRgxQsXFxVq5cuUZzY0KBAAAdcjj8ai0tNRv83g8Z/TakpISSVKzZs0kSXl5eaqqqlJKSopvTLt27dS6dWvl5ORIknJyctSpUydfeJCk1NRUlZaWaufOnb4xPzzHiTEnznEmCBAAAJhCHAHbsrKyFBUV5bdlZWVZTqGmpkbjx4/XFVdcoUsuuUSS5Ha7FRERoejoaL+xsbGxcrvdvjE/DA8njp84droxpaWlOnbs2BldIu7CAADAFMCbMCZNmqTMzEy/fU6n0/J16enp2rFjh/7zn/8EbjIBRIAAAKAOOZ3OMwoMP5SRkaHly5dr/fr1Ou+883z7XS6XKisrVVxc7FeFKCwslMvl8o3Jzc31O9+JuzR+OMa8c6OwsFCRkZFq2LDhGc2RFgYAACaHI3CbDV6vVxkZGXr99de1du1aJSQk+B1PTExUeHi41qxZ49u3e/duFRQUKDk5WZKUnJys7du36+DBg74x2dnZioyMVIcOHXxjfniOE2NOnONMUIEAAMAUpCdRpqen66WXXtK//vUvNWnSxLdmISoqSg0bNlRUVJTS0tKUmZmpZs2aKTIyUuPGjVNycrJ69OghSerXr586dOigW265RdOnT5fb7daDDz6o9PR0XyXkrrvu0rx583Tffffp9ttv19q1a/Xyyy9rxYoVZzxXKhAAANQTTz/9tEpKSnTVVVcpLi7Oty1dutQ3ZubMmRo0aJCGDx+u3r17y+Vy6bXXXvMdDw0N1fLlyxUaGqrk5GT99re/1ejRozVt2jTfmISEBK1YsULZ2dnq3LmznnjiCT377LNKTU0947nyHAigHuM5EMCp1PFzIG74R8DOteeV3wbsXPUJLQwAAEx8mZYlAgQAACbygyXWQAAAANuoQAAAYPDydd6WCBBnmXvTh2pY/+66+FfxOlZRqc15n+jPWUv06edfn3T8skX3K7VPF914xxN6c9VW3/6rruioKX+8UR3btVL5UY8W/3O9pkxfqurqGklS6/NaaPfGubXOd+XQ/1HuB3vq5s0Bdezqq9P05ZcHa+2/+eZrNWXK3Zo8eZ42btymgweL1KhRA3Xt2l733jtGv/pVqyDMFnWKNRCWCBBnmV5J7fXMolXK+/BzhYWG6KH7Rmj5Pyapa9+JOnrM/8tbxqUN0MluwunUvrWWLbxff523TGkTnlK8q5nmPpqm0JAQTfrLYr+xA0Y+oo8/+cL385FvyurmjQE/g1dffdIXkiXp00/367bb/kf9+/eUJHXseKEGD75KcXEtVVLyrebOXaK0tMlas+ZZhYaGBmvaQFAQIM4yQ0c/5vfz2D8+rQP5C9S1U4I25O7y7b+0QxvdM3agrhj0Z+3Le8bvNdcPTtaOXQXKmv3dfcWf7y/Un7Ne0j+eukd/mfVPlZVX+MYWfVOmwkMldfiOgJ9Ps2ZRfj8vWPCqWreO02WXffdFRjfd1N937LzzYjV+/G81dOgf9OWXB9W6ddzPOlfUMQoQllhEeZaLbNJIkvRN8feVgYYNIrRwbobGP/jCSf/4OyPCVeGp8tt3rKJSDRtEqGsn/8eqvvrcvdr//jNa888pGnhNYh28AyA4Kiur9MYb72r48BQ5TlLOPnq0Qq+9tlrnnRcrl6tFEGaIOhXAb+M8W9muQBw+fFjPP/+8cnJyfI/YdLlcuvzyy3XrrbeqZcuWAZ8kfhyHw6HHp47Wxi279NEP2gzTp9yiTVs/0fLsvJO+Lvu9bcpIG6Abh1yuV5fnyNUyWg/cc50kKS6mqSSpvNyj+6f9XTlbd6umxqth116ml/+WqRvvfFIrTnFe4L/J6tWb9O235frNb/r67V+8eIVmzFioo0crlJBwrl544WFFRIQHaZZA8NgKEFu2bFFqaqoaNWqklJQUXXzxd08CKyws1Jw5c/TYY4/pnXfeUbdu3U57Ho/HI4/Hvx/v9VbL4aCHGEizHrlNHS9upb7Dp/r2DbwmUVdd3lE9Bkw65evW/Hu7HvjLYs15NE3Pzfq9PJVVemzO6+qZ1F413u/6w0e++VZznn3L95q8Dz9XXGxTTfjdIAIEzgr//Ge2evdOVGxsc7/9Q4ZcpSuu6KpDh4r03HOva/z4v2rJkulyOiOCNFPUCRZRWrIVIMaNG6cbbrhBzzzzTK2Sntfr1V133aVx48YpJyfntOfJysrSQw/5P6I3NLKjwqM62ZkOTmPmtFt1bd9fK+WGh/Slu8i3/6rLO+qCNrFy73jOb/yS/52gDbm7lHrTw5KkOc++pTnPvqW42Kb6prhMbVq11MN/Gqm9+2uvUD9hywd7dHUv/jvEf78vvzyojRu3ae7c2kG7SZPGatKksc4/P16dO7fVZZeNVHZ2jgYNujIIM0WdIT9YshUgtm3bpoULF560H+hwODRhwgR17drV8jyTJk1SZmam376YjnfYmQpOY+a0WzWkf3f1u/Fh7T9wyO/YjKf+pReWrPXbl7f6cd037UWtWP1+rXN9XfiNJOnGIZfrwJeH9cGOvaf8vZd2PF/uwuKf/gaAIHvttdVq3jxKV13V3XKs1+tVZWWV5TjgbGMrQLhcLuXm5qpdu3YnPZ6bm6vY2FjL8zidTt9Xip5A+yIwZj1yu24aerluuOMJlZUfU2zL71aVl5QeVYWnSoWHSk66cPLAl0f8wsaE3w3SqnXbVOP1amj/7rr390P129/PVk3Nd7d9jrq+t6oqjyt/5z5J0tD+3TXmxqt0930L6v5NAnWopqZGr722WsOGXa2wsO//f+nAAbfeeuvfuuKKrmrWLFJu9xEtWPCqGjRw6sorT9+2xX+hs3jxY6DYChD33nuvxo4dq7y8PPXt29cXFgoLC7VmzRr97W9/04wZM+pkojgzvxt9jSQp+5XJfvvvzHxa/3h1/Rmfp99VXXRfxjA5neHa/tF+3XDHDK1at81vzJ/u+Y1an9tCx4/X6JPPvtIt6bP1+lu5P/1NAEG0cWO+vvrqkIYPv8Zvf0REuLZu3alFi95QaWmZmjePVrduHbVkyXQ1bx4dnMmi7hAgLNn+Ou+lS5dq5syZysvLU3V1taTvvns8MTFRmZmZuvHGG3/URPg6b6A2vs4bOJW6/TrvC+54JWDn+vzZGwJ2rvrE9m2cN910k2666SZVVVXp8OHDkqQWLVooPJzbmAAA+KX40U+iDA8PV1wcT14DAJyFaGFY4lHWAACYeA6EJR5lDQAAbKMCAQCAiRaGJQIEAAAm6vOWuEQAAMA2KhAAAJhYRGmJAAEAgIk1EJZoYQAAANuoQAAAYPDSwrBEgAAAwER93hIBAgAAE2sgLJGxAACAbVQgAAAwsQbCEgECAAATLQxLtDAAAIBtVCAAADBRgLBEgAAAwOClhWGJFgYAALCNCgQAACYqEJYIEAAAmLiN0xItDAAAYBsVCAAATHy8tkSAAADARAvDEgECAAATiygtUaQBAAC2UYEAAMBEBcISAQIAAIOXNRCWaGEAAADbqEAAAGDi47UlAgQAACZaGJbIWAAAwDYqEAAAmLgLwxIBAgAAEwHCEi0MAABgGxUIAABMFCAsESAAADB4aWFYIkAAAGDiNk5LrIEAAAC2UYEAAMBEC8MSAQIAABP5wRItDAAAYBsVCAAADCF8vLZEgAAAwMBNGNbIWAAAwDYqEAAAGKhAWCNAAABgcJAgLBEgAAAwkB+ssQYCAADYRoAAAMDgcARus2P9+vUaPHiw4uPj5XA4tGzZMr/jt956qxwOh9/Wv39/vzFFRUUaNWqUIiMjFR0drbS0NJWVlfmN+fDDD9WrVy81aNBArVq10vTp021fIwIEAAAGR0jgNjvKy8vVuXNnzZ8//5Rj+vfvr6+//tq3LVmyxO/4qFGjtHPnTmVnZ2v58uVav369xo4d6zteWlqqfv36qU2bNsrLy9Pjjz+uqVOnasGCBbbmyhoIAADqiQEDBmjAgAGnHeN0OuVyuU567OOPP9bKlSu1ZcsWdevWTZI0d+5cXXvttZoxY4bi4+O1ePFiVVZW6vnnn1dERIQ6duyo/Px8Pfnkk35BwwoVCAAADMFqYZyJdevWKSYmRm3bttXdd9+tI0eO+I7l5OQoOjraFx4kKSUlRSEhIdq8ebNvTO/evRUREeEbk5qaqt27d+ubb74543lQgQAAwBDIL+P0eDzyeDx++5xOp5xOp+1z9e/fX9ddd50SEhL02Wef6YEHHtCAAQOUk5Oj0NBQud1uxcTE+L0mLCxMzZo1k9vtliS53W4lJCT4jYmNjfUda9q06RnNhQoEAAB1KCsrS1FRUX5bVlbWjzrXiBEjNGTIEHXq1EnDhg3T8uXLtWXLFq1bty6wkz4DVCAAADAEsvUwadIkZWZm+u37MdWHk7ngggvUokUL7dmzR3379pXL5dLBgwf9xhw/flxFRUW+dRMul0uFhYV+Y078fKq1FSdDBQIAAEMg10A4nU5FRkb6bYEKEF988YWOHDmiuLg4SVJycrKKi4uVl5fnG7N27VrV1NQoKSnJN2b9+vWqqqryjcnOzlbbtm3PuH0hESAAAKg3ysrKlJ+fr/z8fEnS3r17lZ+fr4KCApWVlWnixInatGmT9u3bpzVr1mjo0KG68MILlZqaKklq3769+vfvrzvvvFO5ubnasGGDMjIyNGLECMXHx0uSbr75ZkVERCgtLU07d+7U0qVLNXv27FpVEiu0MAAAMATruzC2bt2qPn36+H4+8Ud9zJgxevrpp/Xhhx9q0aJFKi4uVnx8vPr166eHH37Yr6KxePFiZWRkqG/fvgoJCdHw4cM1Z84c3/GoqCitWrVK6enpSkxMVIsWLTR58mRbt3BKksPr9Xp/4vsNiIatRwZ7CkC9c6zgoWBPAainLq7Ts3d68d8BO9f20b0Cdq76hAoEAAAGvkzLGmsgAACAbVQgAAAwUIGwRoAAAMBAgLBGCwMAANhGBQIAAEMgvwvjbEWAAADAQAvDGi0MAABgGxUIAAAMVCCsESAAADA4WARhiRYGAACwjQoEAAAGWhjWCBAAABgIENYIEAAAGAgQ1lgDAQAAbKMCAQCAgZswrBEgAAAw0MKwRgsDAADYRgUCAACDg4/XlggQAAAYaGFYI2MBAADbqEAAAGBwUIKwRIAAAMBAfrBGCwMAANhGBQIAAAMVCGsECAAADAQIa/UmQBTvnRDsKQD1TuvZXwd7CkC9VHDPxXV6fh5lbY01EAAAwLZ6U4EAAKC+oAJhjQABAIAhxOEN9hTqPVoYAADANioQAAAYaGFYI0AAAGCgPG+NawQAAGyjAgEAgIFFlNYIEAAAGFgDYY0WBgAAsI0KBAAABj5dWyNAAABgoIVhjQABAIDBwSJKS1RpAACAbVQgAAAw0MKwRoAAAMBAed4a1wgAANhGBQIAAANPorRGgAAAwMAaCGu0MAAAgG1UIAAAMPDp2hoBAgAAAy0Ma4QsAABgGxUIAAAM3IVhjQABAICBFoY1AgQAAAb6+9a4RgAAwDYqEAAAGFgDYY0AAQCAgTUQ1mhhAAAA26hAAABgoAJhjQABAICB8rw1rhEAALCNCgQAAAbuwrBGgAAAwMAaCGu0MAAAgG1UIAAAMPDp2hoBAgAAAy0MawQIAAAMDhZRWqJKAwBAPbF+/XoNHjxY8fHxcjgcWrZsmd9xr9eryZMnKy4uTg0bNlRKSoo+/fRTvzFFRUUaNWqUIiMjFR0drbS0NJWVlfmN+fDDD9WrVy81aNBArVq10vTp023PlQABAIAhxBG4zY7y8nJ17txZ8+fPP+nx6dOna86cOXrmmWe0efNmNW7cWKmpqaqoqPCNGTVqlHbu3Kns7GwtX75c69ev19ixY33HS0tL1a9fP7Vp00Z5eXl6/PHHNXXqVC1YsMDWXGlhAABgCNan6wEDBmjAgAEnPeb1ejVr1iw9+OCDGjp0qCTpxRdfVGxsrJYtW6YRI0bo448/1sqVK7VlyxZ169ZNkjR37lxde+21mjFjhuLj47V48WJVVlbq+eefV0REhDp27Kj8/Hw9+eSTfkHDChUIAADqkMfjUWlpqd/m8Xhsn2fv3r1yu91KSUnx7YuKilJSUpJycnIkSTk5OYqOjvaFB0lKSUlRSEiINm/e7BvTu3dvRURE+MakpqZq9+7d+uabb854PgQIAAAMIQ5vwLasrCxFRUX5bVlZWbbn5Ha7JUmxsbF++2NjY33H3G63YmJi/I6HhYWpWbNmfmNOdo4f/o4zQQsDAABDIG/jnDRpkjIzM/32OZ3OwP2CICFAAABQh5xOZ0ACg8vlkiQVFhYqLi7Ot7+wsFBdunTxjTl48KDf644fP66ioiLf610ulwoLC/3GnPj5xJgzQQsDAABDsO7COJ2EhAS5XC6tWbPGt6+0tFSbN29WcnKyJCk5OVnFxcXKy8vzjVm7dq1qamqUlJTkG7N+/XpVVVX5xmRnZ6tt27Zq2rTpGc+HAAEAgCE0gJsdZWVlys/PV35+vqTvFk7m5+eroKBADodD48eP1yOPPKI33nhD27dv1+jRoxUfH69hw4ZJktq3b6/+/fvrzjvvVG5urjZs2KCMjAyNGDFC8fHxkqSbb75ZERERSktL086dO7V06VLNnj27VpvFCi0MAADqia1bt6pPnz6+n0/8UR8zZowWLlyo++67T+Xl5Ro7dqyKi4vVs2dPrVy5Ug0aNPC9ZvHixcrIyFDfvn0VEhKi4cOHa86cOb7jUVFRWrVqldLT05WYmKgWLVpo8uTJtm7hlCSH1+utF8/r9FTnBnsKQL1z0bxjwZ4CUC8V3HNlnZ7/0fzsgJ3rgS7XBOxc9QkVCAAADHyZljUCBAAABgKENRZRAgAA26hAAABgCKUCYYkAAQCAgRaGNVoYAADANioQAAAYQhz14gkH9RoBAgAAAy0Ma7QwAACAbVQgAAAw2P0Oi18iAgQAAAZaGNZoYQAAANuoQAAAYOAuDGsECAAADDyJ0hoBAgAAA2sgrLEGAgAA2EYFAgAAAxUIawQIAAAMBAhrtDAAAIBtVCAAADCEchunJQIEAAAGyvPWuEYAAMA2KhAAABhYRGmNAAEAgIEAYY0WBgAAsI0KBAAABu7CsEaAAADAQAvDGgECAAADAcIaayAAAIBtVCAAADBQgbBGgAAAwBBKgLBECwMAANhGBQIAAEMIt3FaIkAAAGCgPG+NawQAAGyjAgEAgIG7MKwRIH4Btm7dpYXPr9DHO/fp0KFizZpzj65O6eY7fuRwiWY++X/K2bBD3357VL/u1laTHhitNue7fGMOHyrWkzP+Tzkbd6j86DGdf36c7vzdUF3Tr3sw3hJg22XxUborsZU6xZyj2HOcuuPNHVr1+RHf8SeuaasbOrj8XrNuX5FG/2u77+eE6Ib6c88L1C0+SuEhDu06Uq4ZOfuU80WxJOn69rF6sl+7k/7+rgs26sixqsC/MdQJ7sKwRoD4BTh21KO2bVvrN9ddqQl/mO13zOv16p5xsxQWFqrZ8yao8TkN9feFb2ts2mN6/c3H1KhRA0nSnyf9r7799qjmzJ+gpk2b6K0VGzUxc66WvDxN7TucH4R3BdjTKDxUHx0u09KPvtbfBl1y0jHv7ivSvdm7fD9XVvsvpHthyCXaW3xMI17bporjNUrrcq5eGHKJei3crENHq/TmJ4f03v4iv9c8cU07OcNCCA8467AG4hegV+/OGnfPDer7g6rDCfv3u/Xhtj16cPKtuqTTBUpIiNODU25VhadSb7+1yTcu/4NPNXLUNep06a90XqsYjb1rmJo0aayPPtr3M74T4Mdbt79IM3L26Z3PjpxyTGV1jQ4drfJtJZ7jvmNNG4TpgqaN9PTWA9p1uFz7io/psQ171Sg8VG2bN5YkeYzXV3uly1tFa+nOr+v8/SGwQhzegG1nKwLEL1xl5Xf/B+l0hvv2hYSEKCIiXB+8v9u3r0vXi/TO25tVUlymmpoavf1WjjyVlerevf3PPmegrvQ4L1rv35msd0d311/6XKToBt8Xab+pOK49RUc1vH2sGoaFKNQhjeoUp0NHK7X9YNlJzze8XayOHa/Rik8P/1xvAQES4gjcdraihfELl5AQp7i45po982VNnnq7GjZ06u8vrlShu0iHD5X4xj3+ZIbu++N89br8boWFhapBgwjNmjNerdvEBnH2QOCs21+klXsOq6C0Qm2iGuj+yxP04tBOGvbyB6r5/x8ib359m54ddIk+/n1P1XilI0crNXrZdr9KxQ+N6OjSv3YXylNd8zO+EwTC2fyHP1ACXoE4cOCAbr/99tOO8Xg8Ki0t9ds8nspATwVnIDw8TDPn3KP9+9zqmXyXLktMU27uR+rZ61I5HN//C5o/558qLS3Xguf+pCUvP6RbxvTXxMx5+uSTA0GcPRA4b35ySNl7j2j3kXKt+vyIbntjh7q4IpV8XrRvzCNXXaTDxyp1/Sv5GvJ/7+udzw/r+cGXKKZRRK3z/doVqYuaN9bSne6f8V0AP5+AB4iioiItWrTotGOysrIUFRXlt01/7PSvQd3p0DFBr7z+F23Y/L9a895cPbPgPhUXl+m8Vi0lSQcKCrXkpWxNe+RO9UjuqLbt2uju9OvUoWOClr60OsizB+pGQWmFjhyt1PlRDSVJV7SKVt+E5sp4+2Nt/bpUOw6V6cF396iiulrXd6hdiRtxiUs7Dn57yvYG6reQAG5nK9stjDfeeOO0xz///HPLc0yaNEmZmZnGTD60OxUEWJMmjSRJ+/e59dHOvcr4w/WSpGMV31WHQoyaXmhoiGq8lGZxdnKdE6GmDcN1sPy7//03DAuVJNV4/RfF1XjlV62TpEbhIRp0UUv9dcPen2eyCDgHLQxLtgPEsGHD5HA45PWeemWp+Y/J5HQ65XQ6/fZ5qmuXABEYR8srVFBQ6Pv5yy8PadfH+xUV1Vhx8S20auVmNW0Wqbi45vr0kwP6a9Y/1Kdvoi6/opOk79ZJtG4dq2lTX9AfJ45UdPQ5WrsmTzkbd2jeU5mn+rVAvdIoPMRXTZCkVlEN1KFFYxV7jqu4okrjk87X23sO6VB5pdpEN9QDV1ygfcXH9F7Bd7dl5n1dohLPcT3Zr51mb96viuM1GnlJnFpFNtDavf53dgy+OEZhIQ69vqtQwNnK4T1dEjiJc889V0899ZSGDh160uP5+flKTExUdXW1rYl4qnNtjceZ25L7sdJufbTW/iHDeuqRR3+nxX9/RwtfeEtHDpeoZctoDR7aU7+7a5jCI77Pl/v3uTVr5lJ98P4nOnq0Qq1bx2rMbddq8JCeP+db+cW5aN6xYE/hrNHj3Ci9fH2XWvtf+citB9Z+qmcHd1THluco0hmmwvJK/Xt/kWZs2qfDR79/fsOlMedo4uUJujSmicJCHPqk6Khmb96vdcazH167oYsOlFbonnd2mb8OAVJwz5V1ev4th1YE7FzdWw4M2LnqE9sBYsiQIerSpYumTZt20uPbtm1T165dVVNjr7RNgABqI0AAJ1fXAWLr4cAFiG4tzs4AYbuFMXHiRJWXl5/y+IUXXqh33333J00KAADUb7YDRK9evU57vHHjxrryyrpNhgAA1KWz+e6JQOFBUgAAGBxn8SOoA4WQBQAAbKMCAQCAgcdAWCNAAABg4EFS1ggQAAAYyA/WWAMBAABsowIBAICBr/O2RoAAAMBAfrBGCwMAANhGBQIAAAN3YVgjQAAAYCA/WKOFAQAAbKMCAQCAgQqENQIEAAAGbuO0RgsDAADYRgUCAAADBQhrVCAAADA4HN6AbXZMnTpVDofDb2vXrp3veEVFhdLT09W8eXOdc845Gj58uAoLC/3OUVBQoIEDB6pRo0aKiYnRxIkTdfz48YBclx+iAgEAgCGYFYiOHTtq9erVvp/Dwr7/Uz1hwgStWLFCr7zyiqKiopSRkaHrrrtOGzZskCRVV1dr4MCBcrlc2rhxo77++muNHj1a4eHhevTRRwM6TwIEAAD1SFhYmFwuV639JSUleu655/TSSy/p6quvliS98MILat++vTZt2qQePXpo1apV+uijj7R69WrFxsaqS5cuevjhh3X//fdr6tSpioiICNg8aWEAAGBwOAK3eTwelZaW+m0ej+eUv/vTTz9VfHy8LrjgAo0aNUoFBQWSpLy8PFVVVSklJcU3tl27dmrdurVycnIkSTk5OerUqZNiY2N9Y1JTU1VaWqqdO3cG9BoRIAAAMIQEcMvKylJUVJTflpWVddLfm5SUpIULF2rlypV6+umntXfvXvXq1Uvffvut3G63IiIiFB0d7fea2NhYud1uSZLb7fYLDyeOnzgWSLQwAACoQ5MmTVJmZqbfPqfTedKxAwYM8P3nSy+9VElJSWrTpo1efvllNWzYsE7naRcVCAAADIFsYTidTkVGRvptpwoQpujoaF188cXas2ePXC6XKisrVVxc7DemsLDQt2bC5XLVuivjxM8nW1fxUxAgAAAwOAK4/RRlZWX67LPPFBcXp8TERIWHh2vNmjW+47t371ZBQYGSk5MlScnJydq+fbsOHjzoG5Odna3IyEh16NDhJ87GHy0MAADqiXvvvVeDBw9WmzZt9NVXX2nKlCkKDQ3VyJEjFRUVpbS0NGVmZqpZs2aKjIzUuHHjlJycrB49ekiS+vXrpw4dOuiWW27R9OnT5Xa79eCDDyo9Pf2Mqx5nigABAIDBEaQHQXzxxRcaOXKkjhw5opYtW6pnz57atGmTWrZsKUmaOXOmQkJCNHz4cHk8HqWmpuqpp57yvT40NFTLly/X3XffreTkZDVu3FhjxozRtGnTAj5Xh9frtfeYrDriqc4N9hSAeueieceCPQWgXiq458o6Pf8X5W8G7FznNR4csHPVJ6yBAAAAttHCAADAwNd5WyNAAABgID9YI0AAAGCw+y2av0SsgQAAALZRgQAAwEALwxoBAgAAQ7CeA/HfhBYGAACwjQoEAAAGChDWCBAAABgoz1vjGgEAANuoQAAAYGARpTUCBAAAtZAgrNDCAAAAtlGBAADA4KACYYkAAQCAweGgQG+FAAEAQC1UIKwQsQAAgG1UIAAAMLAGwhoBAgCAWggQVmhhAAAA26hAAABg4C4MawQIAABqoYVhhYgFAABsowIBAICBuzCsESAAADAQIKzRwgAAALZRgQAAoBY+X1shQAAAYHA4aGFYIUAAAFALAcIKNRoAAGAbFQgAAAzchWGNAAEAQC0U6K1whQAAgG1UIAAAMNDCsEaAAADAwG2c1mhhAAAA26hAAABQCxUIKwQIAAAMDgr0lrhCAADANioQAADUQgvDCgECAAADd2FYI0AAAFALAcIKayAAAIBtVCAAADBwF4Y1AgQAALXQwrBCxAIAALZRgQAAwMCXaVkjQAAAYOA2Tmu0MAAAgG1UIAAAqIXP11YIEAAAGFgDYY2IBQAAbKMCAQBALVQgrBAgAAAwcBeGNQIEAAC10OG3whUCAAC2UYEAAMDAXRjWHF6v1xvsSaD+8Hg8ysrK0qRJk+R0OoM9HaBe4N8FUBsBAn5KS0sVFRWlkpISRUZGBns6QL3AvwugNtZAAAAA2wgQAADANgIEAACwjQABP06nU1OmTGGhGPAD/LsAamMRJQAAsI0KBAAAsI0AAQAAbCNAAAAA2wgQAADANgIEfObPn6/zzz9fDRo0UFJSknJzc4M9JSCo1q9fr8GDBys+Pl4Oh0PLli0L9pSAeoMAAUnS0qVLlZmZqSlTpuj9999X586dlZqaqoMHDwZ7akDQlJeXq3Pnzpo/f36wpwLUO9zGCUlSUlKSunfvrnnz5kmSampq1KpVK40bN05/+tOfgjw7IPgcDodef/11DRs2LNhTAeoFKhBQZWWl8vLylJKS4tsXEhKilJQU5eTkBHFmAID6igABHT58WNXV1YqNjfXbHxsbK7fbHaRZAQDqMwIEAACwjQABtWjRQqGhoSosLPTbX1hYKJfLFaRZAQDqMwIEFBERocTERK1Zs8a3r6amRmvWrFFycnIQZwYAqK/Cgj0B1A+ZmZkaM2aMunXrpssuu0yzZs1SeXm5brvttmBPDQiasrIy7dmzx/fz3r17lZ+fr2bNmql169ZBnBkQfNzGCZ958+bp8ccfl9vtVpcuXTRnzhwlJSUFe1pA0Kxbt059+vSptX/MmDFauHDhzz8hoB4hQAAAANtYAwEAAGwjQAAAANsIEAAAwDYCBAAAsI0AAQAAbCNAAAAA2wgQAADANgIEAACwjQABAABsI0AAAADbCBAAAMA2AgQAALDt/wGfR3LzCxyoIAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "\n",
        "# Define the filename for the pickle file\n",
        "filename = 'Phase 4 Model.pkl'\n",
        "\n",
        "# Save the trained model to a pickle file\n",
        "with open(filename, 'wb') as file:\n",
        "    pickle.dump(rf_clf, file)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "1Cil4vvq8XxD"
      },
      "id": "1Cil4vvq8XxD",
      "execution_count": 93,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.13"
    },
    "colab": {
      "provenance": [],
      "gpuType": "T4"
    },
    "accelerator": "GPU"
  },
  "nbformat": 4,
  "nbformat_minor": 5
}