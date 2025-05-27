# haftalik avtomatlashtirish

import schedule
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    print("🚀 IMDb Data Cleaning and KPI Generation Started")

    # 1. Papkalarni yaratamiz (agar mavjud bo‘lmasa)
    os.makedirs("charts", exist_ok=True)
    os.makedirs("kpis", exist_ok=True)

    # 2. CSV faylni yuklash
    df = pd.read_csv("imdb_top_250_movies_final.csv")

    # 3. Cleaning
    df["Genres"] = df["Genres"].apply(eval)
    df["Cast"] = df["Cast"].apply(eval)
    df["Directors"] = df["Directors"].apply(eval)
    df["Box Office"] = df["Box Office"].replace('[\$,]', '', regex=True).astype(float)

    # 4. Explode qilish
    df_genres = df[["Title", "Genres"]].explode("Genres")
    df_cast = df[["Title", "Cast"]].explode("Cast")
    df_directors = df[["Rating", "Directors"]].explode("Directors")

    # 5. KPI – Top genres
    top_genres = df_genres["Genres"].value_counts().head(10).reset_index()
    top_genres.columns = ["Genre", "Film Count"]
    top_genres.to_csv("kpis/top_10_genres.csv", index=False)

    # 6. KPI – Top actors
    top_actors = df_cast["Cast"].value_counts().head(10).reset_index()
    top_actors.columns = ["Actor", "Film Count"]
    top_actors.to_csv("kpis/top_10_actors.csv", index=False)

    # 7. KPI – Top directors by rating
    top_directors = (
        df_directors.groupby("Directors")["Rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    top_directors.columns = ["Director", "Average Rating"]
    top_directors.to_csv("kpis/top_10_directors.csv", index=False)

    # 8. KPI – Yearly average rating
    yearly_avg = df.groupby("Year")["Rating"].mean().reset_index()
    yearly_avg.to_csv("kpis/yearly_avg_rating.csv", index=False)

    print("✅ KPI CSV fayllar 'kpis/' papkaga saqlandi.")

    # 9. Grafik – Top Genres
    plt.figure(figsize=(10,6))
    plt.bar(top_genres["Genre"], top_genres["Film Count"], color='skyblue')
    plt.title("Top 10 Most Frequent Genres")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/top_10_genres_chart.png")

    print("📊 Grafik saqlandi: charts/top_10_genres_chart.png")

    print("🏁 Barcha bosqichlar muvaffaqiyatli yakunlandi.")



# Har haftaning dushanba kuni 09:00 da ishga tushadi
schedule.every().monday.at("09:00").do(main)

# Doimiy kutish sikli
while True:
    schedule.run_pending()
    time.sleep(60)

#Faqat bajarish:

main()

#Avtomatik ishga tushirish (har dushanba soat 09:00 da):

import schedule
import time

schedule.every().monday.at("09:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(60)
