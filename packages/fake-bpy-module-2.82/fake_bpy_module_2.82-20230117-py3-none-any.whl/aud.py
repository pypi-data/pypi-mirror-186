import sys
import typing

GenericType = typing.TypeVar("GenericType")


class Device:
    ''' Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output. lock() Locks the device so that it's guaranteed, that no samples are read from the streams until :meth:`unlock` is called. This is useful if you want to do start/stop/pause/resume some sounds at the same time. play(sound, keep=False) Plays a sound. :arg sound: The sound to play. :type sound: `Sound` :arg keep: See :attr:`Handle.keep`. :type keep: bool :return: The playback handle with which playback can be controlled with. :rtype: `Handle` stopAll() Stops all playing and paused sounds. unlock() Unlocks the device after a lock call, see :meth:`lock` for details.
    '''

    channels = None
    ''' The channel count of the device.'''

    distance_model = None
    ''' The distance model of the device.'''

    doppler_factor = None
    ''' The doppler factor of the device. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.'''

    format = None
    ''' The native sample format of the device.'''

    listener_location = None
    ''' The listeners's location in 3D space, a 3D tuple of floats.'''

    listener_orientation = None
    ''' The listener's orientation in 3D space as quaternion, a 4 float tuple.'''

    listener_velocity = None
    ''' The listener's velocity in 3D space, a 3D tuple of floats.'''

    rate = None
    ''' The sampling rate of the device in Hz.'''

    speed_of_sound = None
    ''' The speed of sound of the device. The speed of sound in air is typically 343.3 m/s.'''

    volume = None
    ''' The overall volume of the device.'''


class DynamicMusic:
    ''' The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions. The default transition is a crossfade effect, and the default scene is silent and has id 0 addScene(scene) Adds a new scene. :arg scene: The scene sound. :type scene: `Sound` :return: The new scene id. :rtype: int addTransition(ini, end, transition) Adds a new scene. :arg ini: the initial scene foor the transition. :type ini: int :arg end: The final scene for the transition. :type end: int :arg transition: The transition sound. :type transition: `Sound` :return: false if the ini or end scenes don't exist, true othrwise. :rtype: bool pause() Pauses playback of the scene. :return: Whether the action succeeded. :rtype: bool resume() Resumes playback of the scene. :return: Whether the action succeeded. :rtype: bool stop() Stops playback of the scene. :return: Whether the action succeeded. :rtype: bool
    '''

    fadeTime = None
    ''' The length in seconds of the crossfade transition'''

    position = None
    ''' The playback position of the scene in seconds.'''

    scene = None
    ''' The current scene'''

    status = None
    ''' Whether the scene is playing, paused or stopped (=invalid).'''

    volume = None
    ''' The volume of the scene.'''


class Handle:
    ''' Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles. pause() Pauses playback. :return: Whether the action succeeded. :rtype: bool resume() Resumes playback. :return: Whether the action succeeded. :rtype: bool stop() Stops playback. :return: Whether the action succeeded. :rtype: bool
    '''

    attenuation = None
    ''' This factor is used for distance based attenuation of the source.'''

    cone_angle_inner = None
    ''' The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:`location` of the source and with infinite height, heading in the direction of the source's :attr:`orientation`. In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:`cone_volume_outer` and in the area between the volume will be interpolated linearly.'''

    cone_angle_outer = None
    ''' The opening angle of the outer cone of the source.'''

    cone_volume_outer = None
    ''' The volume outside the outer cone of the source.'''

    distance_maximum = None
    ''' The maximum distance of the source. If the listener is further away the source volume will be 0.'''

    distance_reference = None
    ''' The reference distance of the source. At this distance the volume will be exactly :attr:`volume`.'''

    keep = None
    ''' Whether the sound should be kept paused in the device when its end is reached. This can be used to seek the sound to some position and start playback again.'''

    location = None
    ''' The source's location in 3D space, a 3D tuple of floats.'''

    loop_count = None
    ''' The (remaining) loop count of the sound. A negative value indicates infinity.'''

    orientation = None
    ''' The source's orientation in 3D space as quaternion, a 4 float tuple.'''

    pitch = None
    ''' The pitch of the sound.'''

    position = None
    ''' The playback position of the sound in seconds.'''

    relative = None
    ''' Whether the source's location, velocity and orientation is relative or absolute to the listener.'''

    status = None
    ''' Whether the sound is playing, paused or stopped (=invalid).'''

    velocity = None
    ''' The source's velocity in 3D space, a 3D tuple of floats.'''

    volume = None
    ''' The volume of the sound.'''

    volume_maximum = None
    ''' The maximum volume of the source.'''

    volume_minimum = None
    ''' The minimum volume of the source.'''


class PlaybackManager:
    ''' A PlabackManager object allows to easily control groups os sounds organized in categories. addCategory(volume) Adds a category with a custom volume. :arg volume: The volume for ther new category. :type volume: float :return: The key of the new category. :rtype: int clean() Cleans all the invalid and finished sound from the playback manager. getVolume(catKey) Retrieves the volume of a category. :arg catKey: the key of the category. :type catKey: int :return: The volume of the cateogry. :rtype: float pause(catKey) Pauses playback of the category. :arg catKey: the key of the category. :type catKey: int :return: Whether the action succeeded. :rtype: bool setVolume(sound, catKey) Plays a sound through the playback manager and assigns it to a category. :arg sound: The sound to play. :type sound: `Sound` :arg catKey: the key of the category in which the sound will be added, if it doesn't exist, a new one will be created. :type catKey: int :return: The playback handle with which playback can be controlled with. :rtype: `Handle` resume(catKey) Resumes playback of the catgory. :arg catKey: the key of the category. :type catKey: int :return: Whether the action succeeded. :rtype: bool setVolume(volume, catKey) Changes the volume of a category. :arg volume: the new volume value. :type volume: float :arg catKey: the key of the category. :type catKey: int :return: Whether the action succeeded. :rtype: int stop(catKey) Stops playback of the category. :arg catKey: the key of the category. :type catKey: int :return: Whether the action succeeded. :rtype: bool
    '''

    pass


class Sequence:
    ''' This sound represents sequenced entries to play a sound sequence. add() Adds a new entry to the sequence. :arg sound: The sound this entry should play. :type sound: `Sound` :arg begin: The start time. :type begin: float :arg end: The end time or a negative value if determined by the sound. :type end: float :arg skip: How much seconds should be skipped at the beginning. :type skip: float :return: The entry added. :rtype: `SequenceEntry` remove() Removes an entry from the sequence. :arg entry: The entry to remove. :type entry: `SequenceEntry` setAnimationData() Writes animation data to a sequence. :arg type: The type of animation data. :type type: int :arg frame: The frame this data is for. :type frame: int :arg data: The data to write. :type data: sequence of float :arg animated: Whether the attribute is animated. :type animated: bool
    '''

    channels = None
    ''' The channel count of the sequence.'''

    distance_model = None
    ''' The distance model of the sequence.'''

    doppler_factor = None
    ''' The doppler factor of the sequence. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.'''

    fps = None
    ''' The listeners's location in 3D space, a 3D tuple of floats.'''

    muted = None
    ''' Whether the whole sequence is muted.'''

    rate = None
    ''' The sampling rate of the sequence in Hz.'''

    speed_of_sound = None
    ''' The speed of sound of the sequence. The speed of sound in air is typically 343.3 m/s.'''


class SequenceEntry:
    ''' SequenceEntry objects represent an entry of a sequenced sound. move() Moves the entry. :arg begin: The new start time. :type begin: float :arg end: The new end time or a negative value if unknown. :type end: float :arg skip: How many seconds to skip at the beginning. :type skip: float setAnimationData() Writes animation data to a sequenced entry. :arg type: The type of animation data. :type type: int :arg frame: The frame this data is for. :type frame: int :arg data: The data to write. :type data: sequence of float :arg animated: Whether the attribute is animated. :type animated: bool
    '''

    attenuation = None
    ''' This factor is used for distance based attenuation of the source.'''

    cone_angle_inner = None
    ''' The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:`location` of the source and with infinite height, heading in the direction of the source's :attr:`orientation`. In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:`cone_volume_outer` and in the area between the volume will be interpolated linearly.'''

    cone_angle_outer = None
    ''' The opening angle of the outer cone of the source.'''

    cone_volume_outer = None
    ''' The volume outside the outer cone of the source.'''

    distance_maximum = None
    ''' The maximum distance of the source. If the listener is further away the source volume will be 0.'''

    distance_reference = None
    ''' The reference distance of the source. At this distance the volume will be exactly :attr:`volume`.'''

    muted = None
    ''' Whether the entry is muted.'''

    relative = None
    ''' Whether the source's location, velocity and orientation is relative or absolute to the listener.'''

    sound = None
    ''' The sound the entry is representing and will be played in the sequence.'''

    volume_maximum = None
    ''' The maximum volume of the source.'''

    volume_minimum = None
    ''' The minimum volume of the source.'''


class Sound:
    ''' Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback. buffer(data, rate) Creates a sound from a data buffer. :arg data: The data as two dimensional numpy array. :type data: numpy.ndarray :arg rate: The sample rate. :type rate: double :return: The created `Sound` object. :rtype: `Sound` file(filename) Creates a sound object of a sound file. :arg filename: Path of the file. :type filename: string :return: The created `Sound` object. :rtype: `Sound` list() Creates an empty sound list that can contain several sounds. :arg random: wether the playback will be random or not. :type random: int :return: The created `Sound` object. :rtype: `Sound` sawtooth(frequency, rate=48000) Creates a sawtooth sound which plays a sawtooth wave. :arg frequency: The frequency of the sawtooth wave in Hz. :type frequency: float :arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping. :type rate: int :return: The created `Sound` object. :rtype: `Sound` silence(rate=48000) Creates a silence sound which plays simple silence. :arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping. :type rate: int :return: The created `Sound` object. :rtype: `Sound` sine(frequency, rate=48000) Creates a sine sound which plays a sine wave. :arg frequency: The frequency of the sine wave in Hz. :type frequency: float :arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping. :type rate: int :return: The created `Sound` object. :rtype: `Sound` square(frequency, rate=48000) Creates a square sound which plays a square wave. :arg frequency: The frequency of the square wave in Hz. :type frequency: float :arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping. :type rate: int :return: The created `Sound` object. :rtype: `Sound` triangle(frequency, rate=48000) Creates a triangle sound which plays a triangle wave. :arg frequency: The frequency of the triangle wave in Hz. :type frequency: float :arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping. :type rate: int :return: The created `Sound` object. :rtype: `Sound` ADSR(attack,decay,sustain,release) Attack-Decay-Sustain-Release envelopes the volume of a sound. Note: there is currently no way to trigger the release with this API. :arg attack: The attack time in seconds. :type attack: float :arg decay: The decay time in seconds. :type decay: float :arg sustain: The sustain level. :type sustain: float :arg release: The release level. :type release: float :return: The created `Sound` object. :rtype: `Sound` accumulate(additive=False) Accumulates a sound by summing over positive input differences thus generating a monotonic sigal. If additivity is set to true negative input differences get added too, but positive ones with a factor of two. Note that with additivity the signal is not monotonic anymore. :arg additive: Whether the accumulation should be additive or not. :type time: bool :return: The created `Sound` object. :rtype: `Sound` addSound(sound) Adds a new sound to a sound list. :arg sound: The sound that will be added to the list. :type sound: `Sound` cache() Caches a sound into RAM. This saves CPU usage needed for decoding and file access if the underlying sound reads from a file on the harddisk, but it consumes a lot of memory. :return: The created `Sound` object. :rtype: `Sound` data() Retrieves the data of the sound as numpy array. :return: A two dimensional numpy float array. :rtype: `numpy.ndarray` delay(time) Delays by playing adding silence in front of the other sound's data. :arg time: How many seconds of silence should be added before the sound. :type time: float :return: The created `Sound` object. :rtype: `Sound` envelope(attack, release, threshold, arthreshold) Delays by playing adding silence in front of the other sound's data. :arg attack: The attack factor. :type attack: float :arg release: The release factor. :type release: float :arg threshold: The general threshold value. :type threshold: float :arg arthreshold: The attack/release threshold value. :type arthreshold: float :return: The created `Sound` object. :rtype: `Sound` fadein(start, length) Fades a sound in by raising the volume linearly in the given time interval. :arg start: Time in seconds when the fading should start. :type start: float :arg length: Time in seconds how long the fading should last. :type length: float :return: The created `Sound` object. :rtype: `Sound` fadeout(start, length) Fades a sound in by lowering the volume linearly in the given time interval. :arg start: Time in seconds when the fading should start. :type start: float :arg length: Time in seconds how long the fading should last. :type length: float :return: The created `Sound` object. :rtype: `Sound` filter(b, a = (1)) Filters a sound with the supplied IIR filter coefficients. Without the second parameter you'll get a FIR filter. If the first value of the a sequence is 0 it will be set to 1 automatically. If the first value of the a sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don't have to scale yourself. :arg b: The nominator filter coefficients. :type b: sequence of float :arg a: The denominator filter coefficients. :type a: sequence of float :return: The created `Sound` object. :rtype: `Sound` highpass(frequency, Q=0.5) Creates a second order highpass filter based on the transfer function H(s) = s^2 / (s^2 + s/Q + 1) :arg frequency: The cut off trequency of the highpass. :type frequency: float :arg Q: Q factor of the lowpass. :type Q: float :return: The created `Sound` object. :rtype: `Sound` join(sound) Plays two factories in sequence. :arg sound: The sound to play second. :type sound: `Sound` :return: The created `Sound` object. :rtype: `Sound` limit(start, end) Limits a sound within a specific start and end time. :arg start: Start time in seconds. :type start: float :arg end: End time in seconds. :type end: float :return: The created `Sound` object. :rtype: `Sound` loop(count) Loops a sound. :arg count: How often the sound should be looped. Negative values mean endlessly. :type count: integer :return: The created `Sound` object. :rtype: `Sound` lowpass(frequency, Q=0.5) Creates a second order lowpass filter based on the transfer function H(s) = 1 / (s^2 + s/Q + 1) :arg frequency: The cut off trequency of the lowpass. :type frequency: float :arg Q: Q factor of the lowpass. :type Q: float :return: The created `Sound` object. :rtype: `Sound` mix(sound) Mixes two factories. :arg sound: The sound to mix over the other. :type sound: `Sound` :return: The created `Sound` object. :rtype: `Sound` modulate(sound) Modulates two factories. :arg sound: The sound to modulate over the other. :type sound: `Sound` :return: The created `Sound` object. :rtype: `Sound` mutable() Creates a sound that will be restarted when sought backwards. If the original sound is a sound list, the playing sound can change. :return: The created `Sound` object. :rtype: `Sound` pingpong() Plays a sound forward and then backward. This is like joining a sound with its reverse. :return: The created `Sound` object. :rtype: `Sound` pitch(factor) Changes the pitch of a sound with a specific factor. :arg factor: The factor to change the pitch with. :type factor: float :return: The created `Sound` object. :rtype: `Sound` rechannel(channels) Rechannels the sound. :arg channels: The new channel configuration. :type channels: int :return: The created `Sound` object. :rtype: `Sound` resample(rate, high_quality) Resamples the sound. :arg rate: The new sample rate. :type rate: double :arg high_quality: When true use a higher quality but slower resampler. :type high_quality: bool :return: The created `Sound` object. :rtype: `Sound` reverse() Plays a sound reversed. :return: The created `Sound` object. :rtype: `Sound` sum() Sums the samples of a sound. :return: The created `Sound` object. :rtype: `Sound` threshold(threshold = 0) Makes a threshold wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0. :arg threshold: Threshold value over which an amplitude counts non-zero. :type threshold: float :return: The created `Sound` object. :rtype: `Sound` volume(volume) Changes the volume of a sound. :arg volume: The new volume.. :type volume: float :return: The created `Sound` object. :rtype: `Sound` write(filename, rate, channels, format, container, codec, bitrate, buffersize) Writes the sound to a file. :arg filename: The path to write to. :type filename: string :arg rate: The sample rate to write with. :type rate: int :arg channels: The number of channels to write with. :type channels: int :arg format: The sample format to write with. :type format: int :arg container: The container format for the file. :type container: int :arg codec: The codec to use in the file. :type codec: int :arg bitrate: The bitrate to write with. :type bitrate: int :arg buffersize: The size of the writing buffer. :type buffersize: int
    '''

    length = None
    ''' The sample specification of the sound as a tuple with rate and channel count.'''

    specs = None
    ''' The sample specification of the sound as a tuple with rate and channel count.'''


class Source:
    ''' The source object represents the source position of a binaural sound.
    '''

    azimuth = None
    ''' The azimuth angle.'''

    distance = None
    ''' The distance value. 0 is min, 1 is max.'''

    elevation = None
    ''' The elevation angle.'''


class ThreadPool:
    ''' A ThreadPool is used to parallelize convolution efficiently.
    '''

    pass


class error:
    pass


AP_LOCATION = None
''' constant value 3
'''

AP_ORIENTATION = None
''' constant value 4
'''

AP_PANNING = None
''' constant value 1
'''

AP_PITCH = None
''' constant value 2
'''

AP_VOLUME = None
''' constant value 0
'''

CHANNELS_INVALID = None
''' constant value 0
'''

CHANNELS_MONO = None
''' constant value 1
'''

CHANNELS_STEREO = None
''' constant value 2
'''

CHANNELS_STEREO_LFE = None
''' constant value 3
'''

CHANNELS_SURROUND4 = None
''' constant value 4
'''

CHANNELS_SURROUND5 = None
''' constant value 5
'''

CHANNELS_SURROUND51 = None
''' constant value 6
'''

CHANNELS_SURROUND61 = None
''' constant value 7
'''

CHANNELS_SURROUND71 = None
''' constant value 8
'''

CODEC_AAC = None
''' constant value 1
'''

CODEC_AC3 = None
''' constant value 2
'''

CODEC_FLAC = None
''' constant value 3
'''

CODEC_INVALID = None
''' constant value 0
'''

CODEC_MP2 = None
''' constant value 4
'''

CODEC_MP3 = None
''' constant value 5
'''

CODEC_OPUS = None
''' constant value 8
'''

CODEC_PCM = None
''' constant value 6
'''

CODEC_VORBIS = None
''' constant value 7
'''

CONTAINER_AC3 = None
''' constant value 1
'''

CONTAINER_FLAC = None
''' constant value 2
'''

CONTAINER_INVALID = None
''' constant value 0
'''

CONTAINER_MATROSKA = None
''' constant value 3
'''

CONTAINER_MP2 = None
''' constant value 4
'''

CONTAINER_MP3 = None
''' constant value 5
'''

CONTAINER_OGG = None
''' constant value 6
'''

CONTAINER_WAV = None
''' constant value 7
'''

DISTANCE_MODEL_EXPONENT = None
''' constant value 5
'''

DISTANCE_MODEL_EXPONENT_CLAMPED = None
''' constant value 6
'''

DISTANCE_MODEL_INVALID = None
''' constant value 0
'''

DISTANCE_MODEL_INVERSE = None
''' constant value 1
'''

DISTANCE_MODEL_INVERSE_CLAMPED = None
''' constant value 2
'''

DISTANCE_MODEL_LINEAR = None
''' constant value 3
'''

DISTANCE_MODEL_LINEAR_CLAMPED = None
''' constant value 4
'''

FORMAT_FLOAT32 = None
''' constant value 36
'''

FORMAT_FLOAT64 = None
''' constant value 40
'''

FORMAT_INVALID = None
''' constant value 0
'''

FORMAT_S16 = None
''' constant value 18
'''

FORMAT_S24 = None
''' constant value 19
'''

FORMAT_S32 = None
''' constant value 20
'''

FORMAT_U8 = None
''' constant value 1
'''

RATE_11025 = None
''' constant value 11025
'''

RATE_16000 = None
''' constant value 16000
'''

RATE_192000 = None
''' constant value 192000
'''

RATE_22050 = None
''' constant value 22050
'''

RATE_32000 = None
''' constant value 32000
'''

RATE_44100 = None
''' constant value 44100
'''

RATE_48000 = None
''' constant value 48000
'''

RATE_8000 = None
''' constant value 8000
'''

RATE_88200 = None
''' constant value 88200
'''

RATE_96000 = None
''' constant value 96000
'''

RATE_INVALID = None
''' constant value 0
'''

STATUS_INVALID = None
''' constant value 0
'''

STATUS_PAUSED = None
''' constant value 2
'''

STATUS_PLAYING = None
''' constant value 1
'''

STATUS_STOPPED = None
''' constant value 3
'''
