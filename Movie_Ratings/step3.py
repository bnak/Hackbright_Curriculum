def similarity(user1, user2):
    u_ratings = {}
    paired_ratings = []
    for r in user1.data:
        u_ratings[r.item_id] = r

    for r in user2.data:
        u_r = u_ratings.get(r.item_id)
        if u_r:
            paired_ratings.append( (u_r.rating, r.rating) )

    if paired_ratings:
        return correlation.pearson(paired_ratings)
    else:
        return 0.0