####################################
import os, sys
from statistics import mode

# point to path
lib_path = os.path.abspath('../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from text_processor import text_processor	# file name
from text_statistics_estimator import text_statistics_estimator

####################################
## main
####################################
if __name__ == "__main__":
    id_text_processor = "Library Agent: Internal Agent <text_processor>"
    id_text_statistics_estimator = "Library Agent: Internal Agent <text_statistics_estimator>"
    print ("=====[" + id_text_processor + " Start]===== \n")
    text_processor_object = text_processor(id_text_processor)

    print("=====[" + id_text_statistics_estimator + " Start]===== \n")
    text_statistics_estimator_object = text_statistics_estimator(id_text_statistics_estimator)

    file_names = ['./data/The_World_as_I_See_it.txt'];
    chosen_file = file_names[0];

    exclude_list = [
        'in', 'the', 'on', 'i', 'and', 'to', 'of', 'a', 'at', 'is',
        'why', 'or', '', '\'', 'may', 'for', '(', ')', ';', 'but',
        'be', 'if', 'an', 'my', 'as', 'can', 'that', 'this', 'you', 'by',
        'not', 'every', 'it', 'then', 'am', 'he', 'was', 'we', 'who', 'his',
        'all', 'him', 'his', 'me', 'there', 'but', 'however', 'they', 'how', 'more',
        'will', 'our', 'has', 'have', 'shall', 'which', 'been', 'its', 'because', 'let',
        'must', 'are', 'is', 'would', 'when', 'did', 'any', 'so', 'only', 'now',
        'than', 'their', 'could', 'from', 'with', 'without', 'your', 'us', 'what', 'had',
        'no', 'were', 'too', 'those', 'these', 'one', 'two', 'three', 'also', 'such',
        'them', 'into', 'before', 'after', 'see', 'last', 'few', 'quite', 'do', 'should',
        'over', 'might', 'could', 'great', 'most', 'other', 'own', 'up', 'good', 'due',
        '1', 'many', 'even', 'much', '', '', '', '', '', '',
        'each', 'less', 'done', 'very', 'some', 'cause', 'give', 'yet',
        'really', 'especially', 'just',
        # ======================================
        'become', 'relations', 'happenings', 'desired', 'accordance', 'deed', 'among', 'made', 'part', 'far',
        'present', 'about', 'feeling', 'out', 'whose', 'against', 'cannot', 'economic', 'whole', 'through',
        'intellectual', 'being', 'always', 'society', 'make',
        'between', 'nothing', 'first', 'same', 'seems', 'still', 'never', 'like',
        # ======================================
        'life', 'europe', 'fate', 'men', 'einstein', 'work', 'individual', 'international', 'political', 'country',
        'jew', 'world', 'jewish', 'dear', 'struggle', 'human', 'jews', 'people', 'man', 'war',
        'state', 'nations', 'sense', 'years', 'way', 'today', 'academy', 'time', 'community', 'moral',
        'scientific', 'palestine', 'jesus', 'christ', 'thousands', 'simple', 'rest', 'revolutionary', '', '',
        'characteristic', 'intellectually', 'destruction', 'german', 'science', 'life', '', '', '', '',
        'opinion', 'germany', 'spirit', 'development', 'countries', 'attitude', 'take', 'himself', 'social', 'nation',
        'fact', 'power', 'things', 'merely', 'service', 'religious', 'mind', 'tradition', 'labour',
        'existence', 'themselves', 'times', 'itself', 'national', 'efforts', 'reason', 'common', 'religion',
        'prussian', 'important', 'long', 'new', 'military',
        'hope', 'given', 'commission', 'public', 'does', 'race', 'therefore', 'form',
        'progress', 'object', 'once', 'america', 'ourselves', 'difficulties', 'success', 'towards', 'disarmament',
        'particularly', 'view',
        'knowledge', 'free', 'case', 'best', 'necessary', 'peace', 'respect', 'interests', 'crisis', 'sciences',
        'under', 'nature',
        'production', 'general', 'based', 'both', 'problems', 'cooperation', 'say', 'order',
        'letter', 'come', 'get', 'sphere', 'freedom', 'french', 'keep', 'industry', 'american',
        'justice', 'thus', 'government', 'bound', 'god', 'thought', 'european', 'look', 'right',
        'here', 'end', 'little', 'achievements', 'culture', 'sort', 'enterprise', 'responsible', 'something',
        'spiritual', 'force',
        'humanity', 'produced', 'influence', 'affairs', 'real', 'believe', 'security', 'university',
        'system', 'valuable', 'able', 'living', 'further', 'certain', 'generation', 'league', 'prevent',
        'another', 'possible', 'support', 'hence', 'particular', 'members', 'whom', 'feel', 'point',
        'organization', 'desire', 'enough', 'civilization', 'upon', 'thing', 'place', 'problem',
        'material', 'duty', 'large', 'beings', 'devoted', 'felt',
        'cultural', 'position', 'difficult', 'call', 'united', 'depends', 'individuals', 'matter',
        # ======================================
        'psychological', 'live', 'course', 'taken', 'above', 'youth', 'brought', "one's", 'goods',
        'where', 'use', 'strength', 'future', 'need', 'find', '1933', 'arbitration', 'situation',
        'powers', 'set', 'court', 'almost', 'methods', 'entirely', 'hand', 'strong', 'responsibility',
        'help', 'research', 'since', 'everything', 'history', 'liberty', 'put', 'following', 'side',
        'workers', 'moment', 'civilized', 'technical', 'during', 'professor', 'nationalism', 'leaders',
        'personal', 'character', 'while', 'machinery', 'truth', 'rather', 'wealth', 'fear', 'working',
        'serve', 'high', 'step', 'days', 'effect', 'said', 'needed', 'compulsory',
        'found', 'alone', 'means', 'france', 'value', 'others', 'doubt', 'kind', 'task', 'conference',
        'education', 'ago', 'sure', 'experience', 'personality', 'confidence', 'happy', 'independent',
        'highest', 'art', 'question', 'hands', 'answer', 'purpose', 'heart', 'true', 'events', 'results',
        'external', 'know', 'friend', 'ever',
    ];

    filtered_tokens = text_processor_object.read_file_return_keyword(chosen_file, exclude_list)
    # print(filtered_tokens)
    print(len(filtered_tokens))

    filtered_tokens_unique = list(set(filtered_tokens));
    # print(len(filtered_tokens_unique))
    print("Calculating keyword frequencies ... ")
    frequencies = text_statistics_estimator_object.get_frequency(filtered_tokens_unique, filtered_tokens);
    print("... done.")
    frequency_target = max(frequencies);
    # frequency_target = 1;
    print("max frequency: " + str(frequency_target))

    keywords_with_the_frequency = text_statistics_estimator_object.get_keywords_with_the_frequency(filtered_tokens_unique, frequencies,
                                                                  frequency_target);
    print("keywords_with_the_frequency: " + str(keywords_with_the_frequency))
    # print (filtered_tokens_unique[2372])

    # print(filtered_tokens_unique.index('moral'))
    # print(filtered_tokens_unique[121]);
    print("The frequency range is : " + str(max(frequencies)) + " and " + str(min(frequencies)))
    print("The most common frequency is : " + str(mode(frequencies)))
    print("The frequencies are : " + str(list(set(frequencies))))
    print("====================================================================");
    frequency_upper = 11;
    frequency_lower = 9;
    [keywords_within_frequency_range,
     keywords_frequencies_within_frequency_range] = text_statistics_estimator_object.get_keywords_and_frequencies_within_frequency_range(
        filtered_tokens_unique, frequencies, frequency_upper, frequency_lower);
    print("keywords_within_frequency_range: " + str(keywords_within_frequency_range));
    print("keywords_frequencies_within_frequency_range: " + str(keywords_frequencies_within_frequency_range));
    print("====================================================================");
    frequency_upper = 8;
    frequency_lower = 5;
    [keywords_not_within_frequency_range,
     keywords_frequencies_not_within_frequency_range] = text_statistics_estimator_object.remove_keywords_within_frequency_range(filtered_tokens_unique,
                                                                                               frequencies,
                                                                                               frequency_upper,
                                                                                               frequency_lower);
    """
    print("keywords_not_within_frequency_range: " + str(keywords_not_within_frequency_range));
    print("keywords_frequencies_not_within_frequency_range: " + str( keywords_frequencies_not_within_frequency_range));
    """
    print("The frequencies are : " + str(list(set(keywords_frequencies_not_within_frequency_range))))
    print("====================================================================");
    frequency_target = 1;
    [keywords_without_the_frequency, keywords_frequencies_without_the_frequency] = text_statistics_estimator_object.remove_keywords_with_the_frequency(
        filtered_tokens_unique, frequencies, frequency_target);
    """
    print("keywords_without_the_frequency: " + str(keywords_without_the_frequency));
    print("keywords_frequencies_without_the_frequency: " + str( keywords_frequencies_without_the_frequency));
    """
    print("The frequencies are : " + str(list(set(keywords_frequencies_without_the_frequency))))
    print("====================================================================");

    print("=====[" + id_text_statistics_estimator + " End]===== \n")
    print ("=====[" + id_text_processor + " End]===== \n")

    # plot
    import matplotlib

    matplotlib.use('TkAgg')
    # matplotlib.use('ps')

    import numpy as np
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt

    import matplotlib.rcsetup as rcsetup

    print(rcsetup.all_backends)

    plt.figure('Frequencies of words')

    offset, range_length = 20, 5
    plt.xticks(range(0, range_length), filtered_tokens_unique[offset:(offset + range_length)], rotation='vertical')
    degrees = -45 # 45
    # plt.xticks(range(0, range_length), filtered_tokens_unique[offset:(offset + range_length)], rotation=degrees)
    plt.xticks(rotation = degrees)

    plt.plot(frequencies[offset:(offset + range_length)])
    print('The word "', filtered_tokens_unique[offset], '" has frequency of ', frequencies[offset])
    # plt.plot(frequencies)
    # plt.xticks(range(1, len(frequencies)), filtered_tokens_unique, rotation = 'vertical')
    # print ('filtered_tokens: ', filtered_tokens_unique)

    plt.ylabel('filtered_tokens')
    plt.show()

"""
# version: 2017-09-23_2010hr_04sec
"""	